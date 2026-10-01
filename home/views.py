from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import employe
# Create your views here.
def detials(request):
    if request.method=="POST":
        data=employe(request.POST)
        # data=employe.objects.all()
        if data.is_valid():
            name=data.cleaned_data["name"]
            place=data.cleaned_data["place"]
            DOB=data.cleaned_data["DOB"]
            return render(request,"base.html",{
                "data":data,
                "name":name,
                "place":place,
                "DOB":DOB
            })
    else:
        data=employe()
    return render(request,"base.html",{
        "data":data
    })