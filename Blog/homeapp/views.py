from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views import generic
from .models import Contact, Post
from .forms import NewUserForm

# Create your views here.


def index(request):
    return render(request, "index.html")


def contact(request):
	return render(request, "contact.html")

def contact_form(request):
    if request.method == 'POST':
        contact = Contact(name=request.POST["Name"], email=request.POST["Email"], massage=request.POST["Massage"])
        contact.save()
        return render(request, "contact.html",{"res":"Submit Successfully"})
	

def user_register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, "register.html", {"key":"Register Successfully"})
		else:
			return render(request, "register.html", {"key":"Enter valid information"})
	return render(request, "register.html")
def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("postcreate")
			else:
				return render(request,'login.html', {"res":"Invalid username or password."})
		else:
			return render(request,'login.html', {"res":"Invalid username or password."})
	form = AuthenticationForm()
	return render(request, "login.html", context={"login_form":form})


def userlogout(request):
	logout(request)
	return redirect("index")


def about(request):
	return render(request, "about.html")


class PostCreate(generic.CreateView):
	model = Post
	fields = ["author", "title", "content", "status"]
	success_url = "postcreate"

class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'post_list.html'

class Postdetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

