from django.shortcuts import render
from django.views.generic.list import ListView                                # It shows all the tuples stored in the db
from django.views.generic.detail import DetailView                           #It fetch the queried detail from the model with some constraint and show the entire details
from django.views.generic.edit import CreateView,UpdateView,DeleteView      #createview will create the view or insert a record in the table     
from .forms import TaskForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy                       #It redirects to the required url
from django.contrib.auth.mixins import LoginRequiredMixin  #This basically does the authentication stuff for each and every page if it is inherited. For that we need to set the LOGIN_URL in settings to where we want to redirect if not logged in 
from .models import Tasks

class TaskList(LoginRequiredMixin,ListView):         # ListView is a class which as basic functionalities like pulling data from the models by just writing two lines this is way class based view is used
    model = Tasks
    context_object_name = "Tasks"  #Object name that is passed
    template_name = "Todo_list/Tasks.html"

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Tasks
    context_object_name = "Details"
    template_name =  "Todo_list/Details.html"


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Tasks
    fields = '__all__'
    template_name = "Todo_list/create_task.html"
    success_url = reverse_lazy('tasks')

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Tasks
    fields = "__all__"
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

    def get_success_url(self):
        return reverse_lazy('tasks')
