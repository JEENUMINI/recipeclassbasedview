"""RecipeClass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from users.views import UserHome,UserDelete,UserEdit,UserRegistration,UserLogin,Home,SignOut,\
    CreateProfile,UserView

urlpatterns = [
path('userregister',UserRegistration.as_view(),name="userregister"),
path('userlogin',UserLogin.as_view(),name="userlogin"),
path('logout',SignOut.as_view(),name="logout"),
path('home',Home.as_view(),name="home"),
path('userhome',UserHome.as_view(),name="userhome"),
path('profile',CreateProfile.as_view(),name="profile"),
path('delete/<int:pk>',UserDelete.as_view(),name="delete"),
    path('edit/<int:pk>', UserEdit.as_view(), name="edit"),
    path('view/<int:pk>', UserView.as_view(), name="view"),
]
