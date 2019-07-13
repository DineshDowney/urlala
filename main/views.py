from django.shortcuts import render

# Create your views here.
def home(request):
    x=""
    context={"answer": x }
    return render(request,"base.html",context)