from django.shortcuts import render
from main.models import shorted_urls
from main.forms import FormClass
from main.short import short
# Create your views here.
def home(request):
    FormObj = FormClass(request.POST)
    x = ""
    if request.method == 'POST':
        if FormObj.is_valid():
            Url = FormObj.save(commit=False)
            x=short().create_token()
            Url.short_url = x
            Url.save()
    context={"form":FormClass, "x": x }
    return render(request,"base.html",context)
