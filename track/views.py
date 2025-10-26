from django.shortcuts import render, redirect, get_object_or_404
from .models import Track
from student.models import Student

def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'track/track_list.html', {'tracks': tracks})

def track_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Track.objects.create(name=name)
        return redirect('track_list')
    return render(request, 'track/track_form.html')

def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    return render(request, 'track/track_detail.html', {'track': track})

def track_update(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        track.name = request.POST.get('name')
        track.save()
        return redirect('track_list')
    return render(request, 'track/track_form.html', {'track': track})

def track_delete(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        track.delete()
        return redirect('track_list')
    return render(request, 'track/track_confirm_delete.html', {'track': track})

def track_students(request, pk):
    track = get_object_or_404(Track, pk=pk)
    students = Student.objects.filter(track=track)
    return render(request, 'track/track_students.html', {'track': track, 'students': students})
