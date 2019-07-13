from django.shortcuts import render,redirect
from main.models import shorted_urls
from main.forms import FormClass
from main.short import short
# Create your views here

def create_url(request, token):
        url = shorted_urls.objects.filter(short_url=token)[0]
        return redirect(url.long_url)

def home(request):
    FormObj = FormClass(request.POST)
    x = ""
    if request.method == 'POST':
        if FormObj.is_valid():
            Url = FormObj.save(commit=False)
            x=short().create_token()
            Url.short_url = x
            Url.save()
        else:
                FormObj = FormClass()
                x="Invalid URL"
    context={"form":FormObj , "x": x}
    return render(request,"base.html",context)


