from .views import detials
from django.urls import path

urlpatterns = [
    path("form/",detials,name="form")
]