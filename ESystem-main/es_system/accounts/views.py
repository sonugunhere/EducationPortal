from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
from .models import SchoolManagement,StudentRegisteration
from django.contrib import  messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
class Index(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('user_dashboard')
        else:
            return render(request, "home/index.html")
@method_decorator(login_required, name='dispatch')
class UserDashboard(View):
    
    def get(self, request):
        return render(request, "home/dashboard.html")
    
class SchoolRegistration(View):
    
    def get(self, request):
        return render(request, "accounts/register.html")
    
    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        school = request.POST.get("school")
        contact = request.POST.get("contact")
        dise_code = request.POST.get("dise_code")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        school_type = request.POST.get("school_type")
        if (
            (username != "" and username == None)
            or (email != "" and email == None)
            or (password != "" and password == None)
            or (school != "" and school == None)
        ):
            messages.warning(request, "Please enter full detail", "warning")
            return render(request, "accounts/register.html")
        if password == confirm_password:
            if not User.objects.filter(username=username, is_active=True).exists():
                try:
                    users = User.objects.create_user(
                        username=username, password=password, email=email
                    )
                    school_obj = SchoolManagement(
                        user=users,
                        email=email,
                        password=password,
                        confirm_password=confirm_password,
                        username=username,
                        school=school,
                        contact=contact,
                        dise_code=dise_code,
                        address=address,
                        city=city,
                        state=state,
                        country=country,
                        school_type=school_type,
                    )
                    school_obj.save()
                    messages.success(
                        request, "Successfully School Registration", "success"
                    )
                    return redirect('login')
                except Exception as e:
                    print(e)
            else:
                messages.warning(request, "Username already taken", "danger")
                return HttpResponse("Invaild user")
                return redirect("/school_registrations")
        else:
            messages.warning(request, "password not match", "danger")
        return render(request, "accounts/register.html")

class Login(View):
    
    def get(self, request):
        return render(request, "accounts/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username, is_active=True).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged in!")
                return redirect("user_dashboard")
            else:
                messages.warning(request, "Unmatched password !", "danger")
                return redirect("/login")
        else:
                messages.warning(request, "User Not exists !", "danger")
                return redirect("/login")
        
class StudentRegister(View):
    
    def get(self,request):
        school = SchoolManagement.objects.all()
        return render(request, "accounts/student_register.html",{'school':school})
    
    def post(self, request): 
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
        school=request.POST.get('school')
        school_data= SchoolManagement.objects.get(school = school)

        if (
            (first_name != "" and first_name == None) or (email != "" and email == None) or (adhar_card != "" and adhar_card == None) or not (len(contact_no) == 10) ):
            messages.warning(request, "Please enter full detail", "warning")
            #return render(request, "accounts/student_register.html")
        if not StudentRegisteration.objects.filter(adhar_card=adhar_card).exists():
            student_obj = StudentRegisteration(
                        school=school_data, 
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        contact_no=contact_no,
                        father_name=father_name,
                        mother_name=mother_name,
                        address=address,
                        dob=dob,
                        standard=standard,
                        gender=gender,
                        batch=batch,
                        adhar_card=adhar_card
                    )
            student_obj.save()
            messages.success(
                request, "Successfully Student Registration", "success"
            )
            return redirect('student_register')
        else:
            messages.warning(request, "Student already Register", "danger")

            return redirect("student_register")


@method_decorator(login_required, name='dispatch')       
class SchoolLogout(View):
    
    def get(self,request): 
        logout(request)
        return  redirect("login")


