from django.shortcuts import render
from .models import TodoApp

# Create your views here.
def index(request):
    todo = TodoApp.objects.all()
    return render(request,"index.html", {'todos': todo})

def details(request, id):
    todo = TodoApp.objects.get(id=id)
    return render(request,"details.html", {'todos': todo})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        todo =TodoApp(title=title, text=text)
        todo.save()
    else:
        return render(request, "add.html")
