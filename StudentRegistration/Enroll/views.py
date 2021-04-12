from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User


# Create your views here.
def Add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'add.html', {'form': fm, 'student': stud})

def Delete(request,id):
    if request.method == 'POST':
        x=User.objects.get(pk=id)
        x.delete()
        return redirect('/')

def Update(request,id):
    if request.method=='POST':
        x=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=x)
        if fm.is_valid():
            fm.save()
    else:
            x=User.objects.get(pk=id)
            fm=StudentRegistration(instance=x)
    return render(request,'update.html',{'form':fm})
