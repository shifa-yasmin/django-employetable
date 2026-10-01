from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import employe
# Create your views here.
employees=[]
def detials(request):
    delete_id=request.GET.get("delete")
    if delete_id is not None:
        employees.pop(int(delete_id))

    update_id=request.GET.get("update")
    if update_id is not None:
        i=int(update_id)
        data=employe(initial=employees[i])
        return render(request,"base.html",{
            "data":data,
            "employees":employees,
            "update_id":i
        })

    if request.method=="POST":
        data=employe(request.POST)
        
        if data.is_valid():
            employee={
                "name":data.cleaned_data["name"],
                "place":data.cleaned_data["place"],
                "DOB":data.cleaned_data["DOB"]
            }
            update_id=request.POST.get("update_id")
            if update_id is not None:
                employees[int(update_id)]=employee
            else:
                employees.append(employee)
            data=employe()
    else:
        data=employe()
    return render(request,"base.html",{
        "data":data,
        "employees":employees,
        "update_id":None
    })