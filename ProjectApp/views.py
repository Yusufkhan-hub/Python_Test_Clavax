from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm
from django.core.paginator import EmptyPage, Paginator
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def dashboard(request):
    student = Student.objects.all()
    p = Paginator(student,1)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page= p.page(1)
    context = {'items':page}
    return render(request,'dashboard.html',context)



def add_student_details(request):  
    student = Student.objects.all()
    form =  StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request,form.errors)
    else:
        form=StudentForm()
    context = {
        'form':form,
        'student':student}
    return render(request,'upload_details.html',context)

def edit_student_details(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method=='POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        else:
            return render(request,form.errors)
        return redirect('dashboard')
    context = {'form':form}
    return render(request,'upload_details.html',context)

def register_admin(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:   
        form=UserCreationForm()
    context={'form':form}
    return render(request,'registration-admin/registration.html',context)