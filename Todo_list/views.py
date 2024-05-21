from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.list import ListView                                # It shows all the tuples stored in the db
from django.views.generic.detail import DetailView                           #It fetch the queried detail from the model with some constraint and show the entire details
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView      #createview will create the view or insert a record in the table     
from .forms import TaskForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy                       #It redirects to the required url
from django.contrib.auth.mixins import LoginRequiredMixin  #This basically does the authentication stuff for each and every page if it is inherited. For that we need to set the LOGIN_URL in settings to where we want to redirect if not logged in 
from .models import Tasks

class TaskList(LoginRequiredMixin,ListView):         # ListView is a class which as basic functionalities like pulling data from the models by just writing two lines this is way class based view is used
    model = Tasks
    context_object_name = "Tasks"  #Object name that is passed
    template_name = "Todo_list/Tasks.html"
    
    def get_context_data(self, **kwargs):                  #This function filters the data as per the user logged in    
        context = super().get_context_data(**kwargs)                
        context["Tasks"] = context["Tasks"].filter(user = self.request.user)        # context is the object that carries all the tuples in the database and that is being filtered according to the current logged in user
        context["count"] = context["Tasks"].filter(complete = False).count()        # Juz counting the incomplete items
        search = self.request.GET.get('search') or ''
        if search:
            context["Tasks"] = context["Tasks"].filter(title__icontains = search)
        context["search"] = search
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Tasks
    context_object_name = "Details"
    template_name =  "Todo_list/Details.html"


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Tasks
    fields = ['title','desc','complete']
    template_name = "Todo_list/create_task.html"
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):                          #This function sets the user value to the currently logged in user so that we don't show the user option in the form
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Tasks
    fields = ['title','desc','complete']
    template_name = "Todo_list/create_task.html"
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Tasks
    context_object_name = "Tasks"
    template_name = "Todo_list/Delete.html"
    success_url = reverse_lazy('tasks')

class OurLoginView(LoginView):
    template_name = "Todo_list/Login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):                     #If the Login process is successfull then this function will be executed and redirected to the tasks url
        return reverse_lazy('tasks')

class SignUpView(FormView):
    template_name = "Todo_list/signup.html"
    form_class = UserCreationForm
    def get(self,*args,**kwargs):               #  *args recieves the no. of. non-keyword arguments passed and **kwargs recieve the keyword arguments(i.e. Key-value pair arguments) passed to the method
        if self.request.user.is_authenticated:      # This method is used to restrict the authenticated user to see the SignUp page
            return redirect("tasks")
        return super(SignUpView,self).get(*args,**kwargs)              
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):                     #Once the form is created the form_valid method validate the form and save that form by Passing the SignupView to the FormView class This is how we need to send the CustomCreateView to the ParentView 
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)