from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from home.models import contactuser,mydiary
from django.db import IntegrityError
from django.contrib.auth.models import User
import math
# Create your views here.
def index(request):
    try:
        if request.user.is_authenticated:
            return redirect("/dashboard")
        return render (request, "home.html")
    except:
        return HttpResponse("404 Page Not Found")
def contactus(request):
    try:
        if request.method=='POST':
            email=request.POST['email']
            name=request.POST['name']
            address=request.POST['address']
            description=request.POST['description']
            contactuserdetail=contactuser(Name=name , Address = address , Description=description , Email=email)
            contactuserdetail.save()
            messages.success(request,"Thank you!  "+ name +" for contacting Us We will let you soon")
        return render(request, 'contact.html' )
    except:
        messages.error(request, "Something Went wrong")
        return redirect("/")
def diarypage(request):
    try:
        diaryno=12
        
        # print(request.GET.get("page"))
        pageno=request.GET.get("page")
        if pageno==None:
            pageno=1
        else:
            pageno=int(pageno)
        userdiary = mydiary.objects.filter(user=request.user)
        length=len(userdiary)
        userdiary=userdiary[(pageno-1)*diaryno:pageno*diaryno]
        if pageno >1:
            prev=pageno-1
        else:
            prev=None
        if pageno<math.ceil(length/diaryno):
            nxt = pageno+1
        else:
            nxt=None
        context={"userdiary":userdiary,"prev":prev,"next":nxt}
        return render(request, "diary.html",context)
    except:
        return render(request, "diary.html")
def search(request):
    try:
        if request.method=='POST':
            srchstring = request.POST["srchstring"]
            diaryno=12
                # print(request.GET.get("page"))
            pageno=request.GET.get("page")
            if pageno==None:
                pageno=1
            else:
                pageno=int(pageno)
            srchtitle=mydiary.objects.filter(user=request.user).filter(Title__contains=srchstring)
            print(srchtitle)
            srchdescription=mydiary.objects.filter(user=request.user).filter(Description__contains=srchstring)
            print(srchdescription)
            srchdeslug=mydiary.objects.filter(user=request.user).filter(Slug__contains=srchstring)
            print(srchdeslug)
            # srchtime = mydiary.objects.filter(Time=srchstring)
            searchdiary=srchtitle.union(srchdescription,srchdeslug)
            print(searchdiary)
            userdiary = searchdiary
            length=len(userdiary)
            print(length)
            if length==0:
                messages.error(request, "Nothing found related")
                return redirect("/diarypage")
            userdiary=userdiary[(pageno-1)*diaryno:pageno*diaryno]
            if pageno >1:
                prev=pageno-1
            else:
                prev=None
            if pageno<math.ceil(length/diaryno):
                nxt = pageno+1
            else:
                nxt=None
            context={"userdiary":userdiary,"prev":prev,"next":nxt}
            messages.success(request, "Your search results:- ")
            return render(request, "diary.html",context)
        else:
            messages.error(request, "Nothing found related")
            return redirect("/diarypage")
    except:
        messages.success(request, "Your search results")
        return redirect("/diarypage")
def dashboard(request):
    try:
        if request.method=='POST':
            title = request.POST['userdiarytitle']
            description = request.POST['userdiarydescription']
            slug = request.POST['userdiaryslug']
            user = request.user
            diarypage=mydiary(Title=title,Description=description,Short_Description=description[0:200],Slug=slug,user=user)
            diarypage.save()
            messages.success(request, request.user.username+", Your Diary Page is successfully added.")
        return render(request, "userdashboard.html")
    except:
        messages.success(request, "Something Went Wrong")
        return redirect("/")
def handlelogin(request):
    try:
        if request.method=="POST":
            username=request.POST["loginusername"]
            userpassword=request.POST["loginpassword"]
            user = authenticate(username=username,password=userpassword)
            if user is not None:
                    login(request,user)
                    messages.success(request, "You are successfully loged in as "+username)
                    return redirect("/")
            else:
                messages.error(request, "Invalid credentials")
                return redirect("/")
        return redirect("/")
    except:
        messages.success(request, "Something Went Wrong")
        return redirect("/")
def handlelogout(request):
    try: 
        username=request.user
        logout(request)
        messages.success(request, username.username+", you are successfully loged out")
        return redirect("/")
    except:
        messages.success(request, "Something Went Wrong")
        return redirect("/")

def handlesignup (request):
    try:
        if request.method=='POST':
            username=request.POST["username"]
            email=request.POST["email"]
            phonenumber = request.POST["phonenumber"]
            pass1=request.POST["pass1"]
            pass2=request.POST["pass2"]
            myuser = User.objects.create_user(username,email,pass1)

            myuser.save()
            messages.success(request,"Your Account has been Created")
            return redirect("/")
        else:
            messages.error(request, "Something Went wrong")
            return redirect("/")
            
    except IntegrityError :
        messages.error(request, "Username already exist use a different username")
        return redirect("/")
    except:
        messages.error(request, "Something Went wrong")
        return redirect("/") 

def viewdiarypage(request,sno):
    try:
        diarypageread=mydiary.objects.filter(sno=sno).first()
        context={"diarypageread":diarypageread}
        return render(request,"diaryread.html",context)
    except:
        messages.success(request, "Something Went Wrong")
        return redirect("/")

def updatediary(request,sno):
    try:
        diarypageread=mydiary.objects.filter(sno=sno).first()
        if request.method=="POST":
            diarypageread.Title=request.POST['userdiarytitle']
            diarypageread.Description=request.POST['userdiarydescription']
            diarypageread.Short_Description=diarypageread.Description[0:200]
            diarypageread.Slug=request.POST['userdiaryslug']
            diarypageread.user=request.user
            diarypageread.save()
            messages.success(request, "Your diary has successfully updated")
            return redirect("/")
        context={"diarypageread":diarypageread , "updateboard":True}
        return render(request, "update.html",context)
    except:
        messages.success(request, "Something Went Wrong")
        return redirect("/")
def deletediarypage(request,sno):
    try:
        mydiary.objects.filter(sno=sno).delete()
        messages.success(request, "Your diary has successfully deleted")
        return redirect("/")
    except:
        messages.success(request, "Something Went Wrong")
        return redirect("/")