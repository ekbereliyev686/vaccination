from django.shortcuts import render
from .models import Center
# Create your views here.

def center_list(request):
    centers=Center.objects.all()
    context={
        'centers':centers
    }
    return render(request,'center/center_list.html',context)