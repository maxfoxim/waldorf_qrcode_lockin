"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from polls.views import PersonTableView, PersonTableViewSpeichern,post_edit,html_button


urlpatterns = [
    #path("polls/", include("polls.urls")),
    path("polls/", PersonTableView.as_view()),
    path("admin/", admin.site.urls),
    #path('zeitspeichern/', post_edit, name='post_edit')
    #path('zeitspeichern/', PersonTableViewSpeichern.as_view())
    path('zeitspeichern/<int:id>/', post_edit, name='zeitspeichern')
]