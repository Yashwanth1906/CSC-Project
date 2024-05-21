from django.urls import path
from .  import views
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,OurLoginView,LogoutView,SignUpView
urlpatterns = [
    path('',TaskList.as_view(),name="tasks"),
    path('login/',OurLoginView.as_view(),name="login"),
    path('signup/',SignUpView.as_view(),name="signup"),
    path('logout/',LogoutView.as_view(next_page = 'login'),name="logout"),
    path('task/<int:pk>/',TaskDetail.as_view()),
    path('createTask/',TaskCreate.as_view()),
    path('updateTask/<int:pk>/',TaskUpdate.as_view()),
    path('deleteTask/<int:pk>/',TaskDelete.as_view()),
]