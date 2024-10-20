from django.shortcuts import render

# Create your views here.
def home(request):
    #req is used to navgate the command to our html page
    # for navigatin we need to 
    return render(request,'index.html')