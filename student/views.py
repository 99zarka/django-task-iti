from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from track.models import Track

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        image = request.FILES.get('image')
        date_of_birth = request.POST.get('date_of_birth')
        track_id = request.POST.get('track')
        track = get_object_or_404(Track, pk=track_id)
        Student.objects.create(name=name, age=age, image=image, date_of_birth=date_of_birth, track=track)
        return redirect('student_list')
    tracks = Track.objects.all()
    return render(request, 'student/student_form.html', {'tracks': tracks})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student/student_detail.html', {'student': student})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        if request.FILES.get('image'):
            student.image = request.FILES.get('image')
        student.date_of_birth = request.POST.get('date_of_birth')
        track_id = request.POST.get('track')
        student.track = get_object_or_404(Track, pk=track_id)
        student.save()
        return redirect('student_list')
    tracks = Track.objects.all()
    return render(request, 'student/student_form.html', {'student': student, 'tracks': tracks})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student/student_confirm_delete.html', {'student': student})
