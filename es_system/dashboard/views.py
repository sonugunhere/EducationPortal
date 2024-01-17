from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views import View
from accounts.models import StudentRegisteration,SchoolManagement
from django.contrib import  messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required


@method_decorator(login_required, name='dispatch')
class Home(View):
    @login_required(login_url='/user/register')
    def get(request):
        return render(request, "home/dashboard.html")
    

@method_decorator(login_required, name='dispatch')
class CreateStudent(View):
    
    def get(self,request):
        return render(request,'home/student_reg.html')
    
    def post(self,request):
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            contact_no=request.POST.get('contact_no')
            father_name=request.POST.get('father_name')
            mother_name=request.POST.get('mother_name')
            address=request.POST.get('address')
            dob=request.POST.get('dob')
            standard=request.POST.get('standard')
            gender=request.POST.get('gender')
            batch=request.POST.get('batch')
            adhar_card=request.POST.get('adhar_card')
            school = request.user
            school_data=SchoolManagement.objects.filter(user__username = request.user)
            for data in school_data:
                school = SchoolManagement.objects.get(id = data.id)
            students=StudentRegisteration(school=school,adhar_card=adhar_card,first_name=first_name,last_name=last_name,email=email,contact_no=contact_no,father_name=father_name,
                                        mother_name=mother_name,address=address,dob=dob,standard=standard,gender=gender,batch=batch)
            students.save()
            return redirect('student_list')

@method_decorator(login_required, name='dispatch')        
class StudentList(View):
    
    def get(self, request):
        return render(request, "home/student_list.html",{'students':StudentRegisteration.objects.all()})

    def post(self,request):
        txt = request.POST.get('txtsearch')
        if txt:
            query = StudentRegisteration.objects.filter(first_name__istartswith=txt)
            return render(request,'home/student_list.html', {'students':query})
        else:
            return render(request,'home/student_list.html',{'msg':"No data found"})

@method_decorator(login_required, name='dispatch')  
class UpdateStudent(View):
    
    def get(self,request,id):
        student = StudentRegisteration.objects.get(id=id)
        return render(request, "home/student_edit.html", {'student': student})
    
    def post(self,request,id):
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        contact_no=request.POST["contact_no"]
        father_name=request.POST["father_name"]
        mother_name=request.POST["mother_name"]
        address=request.POST["address"]
        standard=request.POST["standard"]
        gender=request.POST["gender"]
        batch=request.POST["batch"] 
        adhar_card=request.POST["adhar_card"]  
        student = StudentRegisteration.objects.get(id=request.POST["txtid"])
        student.first_name=first_name
        student.last_name=last_name
        student.email=email
        student.contact_no=contact_no
        student.father_name=father_name
        student.mother_name=mother_name
        student.address=address
        student.standard=standard
        student.gender=gender
        student.batch=batch
        student.adhar_card=adhar_card
        student.save()
        messages.success(
                        request, "Successfully Update", "success"
                    )
        return redirect('student_list')

@method_decorator(login_required, name='dispatch')       
class StudentDelete(View):
    
    def get(self,request,id):
        student_delete = StudentRegisteration.objects.get(id=id)
        student_delete.delete()
        messages.success(
                        request, "Deleted", "success"
                    )
        return redirect('student_list')
    
