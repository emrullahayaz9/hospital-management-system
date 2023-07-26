from django.shortcuts import render, HttpResponse
from x.models import UsersModel
from . import models

# Create your views here.
def doctor_interface(request, id):
    boolean=False
    bool2 = False
    user = UsersModel.objects.get(pk=id)
    if user.role=="D":
        if request.method=="POST":
            if user.role=="D":
                name = request.POST["name"]
                surname = request.POST["surname"]
                disease_type = request.POST["disease_type"]
                drugs = request.POST["drugs"]
                if name!="" and surname!="" and disease_type!="" and drugs!="":
                    boolean=True
                    models.PatienceInformation(name=name, surname=surname, disease_type=disease_type, drugs=drugs).save()
                    return render(request, "doctor_interface.html", {"boolean":boolean})
        else:
            return render(request, "doctor_interface.html")
    else:
        try:
            bool2 = True
            name = user.username
            info=models.PatienceInformation.objects.get(name=name)
            return render(request, "patience_interface.html", {"info":info, "bool2":bool2})
        except:
            bool2=False
            return render(request, "patience_interface.html", {"info":"your first time", "bool2":bool2})

