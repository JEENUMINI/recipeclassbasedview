from django.shortcuts import render,redirect
from users.forms import ProfileForm,UserRegistrationForm,LoginForm,ProfileCreateForm
from users.models import Profile,ProfileModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView,TemplateView

# Create your views here.
class UserRegistration(TemplateView):
    form_class = UserRegistrationForm()
    template_name = "users/user_form.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class UserLogin(TemplateView):
    form_class = LoginForm()
    template_name = "users/user_login.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
            return redirect("home")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class Home(TemplateView):
    template_name = "users/home.html"

class SignOut(TemplateView):
    template_name = "users/user_login.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("userlogin")

class CreateProfile(TemplateView):
    form =ProfileCreateForm()
    template_name = "users/profile_create.html"
    context={}

    def get(self, request, *args, **kwargs):
        form = ProfileCreateForm()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = ProfileCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

class UserHome(TemplateView):
    model=ProfileModel
    template_name = "users/user_home.html"
    context={}

    def get_query_set(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context["users"]=self.get_query_set()
        return render(request,self.template_name,self.context)

class UserEdit(TemplateView):
    model=ProfileModel
    template_name = "users/user_edit.html"
    context={}

    def get_query_set(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        user=self.get_query_set(kwargs.get("pk"))
        form=ProfileCreateForm(initial={"user":request.user},instance=user)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        user = self.get_query_set(kwargs.get("pk"))
        form = ProfileCreateForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("userhome")



class UserDelete(TemplateView):
    model=ProfileModel

    def get_object(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        user=self.get_object(kwargs.get("pk"))
        user.delete()
        return redirect("userhome")

class UserView(TemplateView):
    model=ProfileModel
    template_name = "users/user_view.html"
    context={}

    def get_query_set(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        user=self.get_query_set(kwargs.get("pk"))
        self.context["user"]=user
        return render(request,self.template_name,self.context)

    # def post(self, request, *args, **kwargs):
    #     user = self.get_query_set(kwargs.get("pk"))
    #     form = ProfileCreateForm(instance=user,data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("userhome")

# user=Profile.objects.get(user=request.user)
#     context={}
#     context["user"]=user
#     return render(request,"users/viewprofile.html",context)