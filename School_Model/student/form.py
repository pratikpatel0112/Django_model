from xml.sax.xmlreader import AttributesImpl
from django import forms

class StudentForm(forms.Form):
    student_name = forms.CharField(label= 'Student Name', widget=forms.TextInput(attrs={'placeholder':'firstname lastname','class':'form-control'}))
    student_email = forms.CharField(label='Student Emailid',widget=forms.EmailInput(attrs={'placeholder':'name@gmail.com','class':'form-control'}))
    student_fees = forms.CharField(label='Student Fees', widget=forms.NumberInput(attrs={'placeholder':'e.g.10000','class':'form-control'}))

