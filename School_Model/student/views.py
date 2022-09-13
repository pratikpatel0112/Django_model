from django.shortcuts import render,redirect
from .models import student
from django.views import View
from .form import StudentForm
from django.contrib import messages
# Create your views here

def index(req):
    return render(req,'student/index.html')

def studentlist(req):
    studlist = student.objects.all()
    response = render(req,'student/studlist.html',{'studlist':studlist})
    return response
    
class add(View):
    def get(self,req):
        studform = StudentForm()
        return render(req,'student/studform.html',{'studform':studform})
    def post(self,req):
        studform = StudentForm(req.POST)
        if studform.is_valid():
            name = studform.cleaned_data['student_name'] 
            email = studform.cleaned_data['student_email']        
            fees = studform.cleaned_data['student_fees']
            stud = student.objects.create(student_name=name, student_email=email , student_fees=fees)
            stud.save()
            messages.success(req,f"{stud.student_name} is add successfully with id {stud.student_id}")
            return redirect('/studlist')
        else:
            return render(req,'student/studform.html',{'studform':studform})

class update(View):
    def get(self,req,id):
        stud = student.objects.get(student_id=id)
        studform = StudentForm(initial = {'student_name':stud.student_name,'student_email':stud.student_email,'student_fees':stud.student_fees})
        return render(req,'student/studform.html',{'studform':studform})
    def post(self,req,id):
        studform = StudentForm(req.POST)
        if studform.is_valid():
            name = studform.cleaned_data['student_name'] 
            email = studform.cleaned_data['student_email']        
            fees = studform.cleaned_data['student_fees']
            stud = student.objects.filter(student_id=id)
            stud.update(student_name=name, student_email=email , student_fees=fees)
            messages.success(req,f"{name} record update successfully")
            return redirect('/studlist')

def delete(req,id):
    if req.method == 'GET':
        stud =  student.objects.get(student_id=id)
        return render(req,'student/confirm.html',{'stud':stud})
    elif req.method == 'POST':
        stud = student.objects.filter(student_id=id)
        stud.delete()
        messages.success(req,f' {stud} student record is deleted')
        return redirect('/studlist')

def nameaes(req):
    studlist = student.objects.order_by('student_name')
    return render(req,'student/studlist.html',{'studlist':studlist})

def namedesc(req):
    studlist = student.objects.order_by('-student_name')
    return render(req,'student/studlist.html',{'studlist':studlist})

def emailaes(req):
    studlist = student.objects.order_by('student_email')
    return render(req,'student/studlist.html',{'studlist':studlist})

def emaildesc(req):
    studlist = student.objects.order_by('-student_email')
    return render(req,'student/studlist.html',{'studlist':studlist})

def feesaes(req):
    studlist = student.objects.order_by('student_fees')
    return render(req,'student/studlist.html',{'studlist':studlist})

def feesdesc(req):
    studlist = student.objects.order_by('-student_fees')
    return render(req,'student/studlist.html',{'studlist':studlist})

    
def searchbyname(req):
    if req.method == 'POST':
        searchnamme = req.POST['searchnamme']
        studlist = student.objects.filter(student_name__istartswith=searchnamme)
        return render(req,'student/studlist.html',{'studlist':studlist})
