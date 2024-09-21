# ajust_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory
from .models import Event, Date, Participant, Response
from .forms import EventForm, DateFormSet, ParticipantForm, ResponseFormSet

def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        date_formset = DateFormSet(request.POST, prefix='dates')
        if event_form.is_valid() and date_formset.is_valid():
            event = event_form.save()
            dates = date_formset.save(commit=False)
            for date in dates:
                date.event = event
                date.save()
            return redirect('event_detail', event_id=event.id)
    else:
        event_form = EventForm()
        date_formset = DateFormSet(prefix='dates')
    return render(request, 'ajust_app/create_event.html', {'event_form': event_form, 'date_formset': date_formset})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    dates = event.dates.all()
    participants = event.participants.all()
    
    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)
        if participant_form.is_valid():
            participant = participant_form.save(commit=False)
            participant.event = event
            participant.save()
            for date in dates:
                Response.objects.create(participant=participant, date=date)
            return redirect('event_detail', event_id=event.id)
    else:
        participant_form = ParticipantForm()

    # 参加可否状況の集計
    date_status = []
    for date in dates:
        yes_count = date.responses.filter(availability='YES').count()
        no_count = date.responses.filter(availability='NO').count()
        maybe_count = date.responses.filter(availability='MAYBE').count()
        date_status.append({
            'date': date,
            'yes': yes_count,
            'no': no_count,
            'maybe': maybe_count
        })

    context = {
        'event': event,
        'dates': dates,
        'participants': participants,
        'participant_form': participant_form,
        'date_status': date_status,
    }
    return render(request, 'ajust_app/event_detail.html', context)

def participant_response(request, event_id, participant_id):
    event = get_object_or_404(Event, id=event_id)
    participant = get_object_or_404(Participant, id=participant_id)
    responses = Response.objects.filter(participant=participant)
    
    if request.method == 'POST':
        formset = ResponseFormSet(request.POST, queryset=responses)
        if formset.is_valid():
            formset.save()
            return redirect('event_detail', event_id=event.id)
    else:
        formset = ResponseFormSet(queryset=responses)
    
    return render(request, 'ajust_app/participant_response.html', {'event': event, 'participant': participant, 'formset': formset})