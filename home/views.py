from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import employe
# Create your views here.
employees=[]
def detials(request):
    if request.method=="POST":
        data=employe(request.POST)
        
        if data.is_valid():
            employees.append({
                "name":data.cleaned_data["name"],
                "place":data.cleaned_data["place"],
                "DOB":data.cleaned_data["DOB"]
            })
            data=employe()
    else:
        data=employe()
    return render(request,"base.html",{
        "data":data,
        "employees":employees
    })