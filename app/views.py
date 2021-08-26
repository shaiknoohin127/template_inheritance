from django.shortcuts import render

# Create your views here.
def mdb(request):
    return render(request,'mdb.html')



def inher_mdb(request):
    return render(request,'inher_mdb.html')