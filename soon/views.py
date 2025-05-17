from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
def soon(request):
    
    # context = {
    #     # 'some': some
    # }
    return render(request, 'soon/index.html')