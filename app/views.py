from django.shortcuts import render
from app.models import App

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def search(request):
    school = request.POST['schoolInput']
    subject = request.POST['subjectInput']
    money = request.POST['moneyInput']
    value = request.POST['valueInput']
    machine = request.POST['machineInput']
    app = App.objects.filter(subject__contains = subject,school__contains = school,money__lte = money,value__gte = value,machine__contains = machine)
    context = {
        'app':app,
    }
    return render(request,"app/search.html",context)