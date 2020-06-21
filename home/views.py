from django.shortcuts import render
from .models import Todo
from django.shortcuts import render_to_response
 
def index(request):
 
    items = Todo.objects.all()
 
    return render_to_response('index.html', {'items': items})