from django.shortcuts import render, redirect
from .forms import employe

employees=[]
def detials(request):
    if request.method=="POST":
        data=employe(request.POST)
        update_id=request.POST.get("update_id")
        if data.is_valid():
            employee={
                "name":data.cleaned_data["name"],
                "place":data.cleaned_data["place"],
                "DOB":data.cleaned_data["DOB"]
            }
            if update_id:
                employees[int(update_id)]=employee
            else:
                employees.append(employee)
            return redirect(request.path)
        return render(request, "base.html", {
            "data":data,
            "employees":employees,
            "update_id":int(update_id)if update_id else None,
        })
    delete_id =request.GET.get("delete")
    if delete_id is not None:
       i=int(delete_id)
       if 0<=i<len(employees):
          employees.pop(i)
       return redirect(request.path)
    
    update_id=request.GET.get("update")
    if update_id is not None:
        i=int(update_id)
        if 0<=i<len(employees):
            return render(request,"base.html", {
                "data":employe(initial=employees[i]),
                "employees":employees,
                "update_id":i,
            })
    return render(request,"base.html",{
        "data":employe(),
        "employees":employees,
        "update_id":None,
    })    