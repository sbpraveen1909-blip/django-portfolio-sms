from django.shortcuts import get_object_or_404, redirect, render
from .models import Student

def student_list(request):
    students = Student.objects.all().order_by("-created_at")
    return render(request, "students/student_list.html", {"students": students})

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            course=request.POST["course"],
            phone=request.POST["phone"],
            address=request.POST["address"],
        )
        return redirect("student_list")
    return render(request, "students/student_form.html")

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.email = request.POST["email"]
        student.course = request.POST["course"]
        student.phone = request.POST["phone"]
        student.address = request.POST["address"]
        student.save()
        return redirect("student_list")

    return render(request, "students/student_form.html", {"student": student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("student_list")