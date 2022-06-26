from django.shortcuts import render,redirect
from django.contrib import messages

from .models import UserData
from django.shortcuts import render
flag=0

def index(request):
    if request.method == "POST":
            name = request.POST['name']
            numberPlate = request.POST['numberPlate']
            contact= request.POST['contact']
            email = request.POST['email']

            print(name, numberPlate, contact, email)
            if UserData.objects.filter(name=name).exists():
                # print("User is already taken")
                # messages.error(request, 'This name is alrady taken')
                return redirect('index')
            elif UserData.objects.filter(numberPlate=numberPlate).exists():
                messages.error(request,"This nummber plate is already registered")
                return redirect('index')
            elif UserData.objects.filter(contact=contact).exists():
                messages.error(request,"contact is already taken")
                return redirect('index')
            elif UserData.objects.filter(email=email).exists():
                messages.error(request,"Email is already taken")
                return redirect('index')
            else:
                students = UserData(name=name, numberPlate=numberPlate, contact=contact,email=email)
                students.save()
                messages.success(request,"you have register succesfully to Parking Portal")
    return render(request,'index.html')


# def index(request):
#     return render(request, 'index.html')




