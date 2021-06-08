from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def addval(request):
    if request.method == 'POST':
        title = request.POST["title"]
        tpass = request.POST["tpass"]
        

    else:
        return render(request,"vault.html")
