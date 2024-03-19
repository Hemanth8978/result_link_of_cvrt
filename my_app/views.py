from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#function for index page or fist page
def index(request):
    return render(request,"index.html",{})

#function for reult page
def result(request):
    from django.db import connection
    cursor=connection.cursor()
    if request.method=="POST":
    
        n=[request.POST.get("htno")]
        
        q="select * from student where stu_htno=%s"
        cursor.execute(q,n)
        for i in cursor:
            
            return render(request,"a1.html",{"cursor":cursor})
        else:
            return HttpResponse("Plese enter valid hall ticket number")
            

        