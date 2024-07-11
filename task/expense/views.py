from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import creditform
from .models import debitform



# Create your views here.
def Home(request):
    return render(request,'Home.html')

def Login(request):
    if request.method == "POST":
        global username
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/Home')
        else:
            messages.info(request, ' Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'Login.html')

def debit(request):
    if request.method == 'POST':
        username = request.user.username
        Beneficiary=request.POST['dfor']
        Amount = request.POST['damount']
        Date = request.POST['ddate']
        Reason = request.POST['dreason']
        Mode=request.POST['dmode']
        Details = request.POST['ddet']
        print(Beneficiary)
        ins2=debitform(username=username,dfor=Beneficiary, damount=Amount, dreason=Reason, ddate=Date, dmode=Mode, ddet=Details)
        ins2.save()
    return render(request,'debit.html')


def ctransactions(request):

    user = request.user.username
    all_credits = creditform.objects.filter(username=user)
    return render(request,'ctransactions.html',{'Credits': all_credits})

def dtransactions(request):
    user = request.user.username
    all_debits = debitform.objects.filter(username=user)
    return render(request,'dtransactions.html',{'Debits': all_debits})

def choose(request):
    return render(request,'choose.html')

def credit(request):

    if request.method == 'POST':
        username =  request.user.username
        Sender=request.POST['cfrom']
        Amount = request.POST['camount']
        Date = request.POST['cdate']
        Reason = request.POST['creason']
        Mode=request.POST['cmode']
        print(Sender)
        ins=creditform(username=username, cfrom=Sender, camount=Amount, creason=Reason, cdate=Date, cmode=Mode)
        ins.save()




    return render(request, 'credit.html',)


def balance(request, sum_credits=None):
    user = request.user.username
    sumcred=0
    sumdeb=0
    balan=0
    all1_credits = creditform.objects.filter(username=user)
    all1_debits = debitform.objects.filter(username=user)
    for credi in all1_credits:
        sumcred=sumcred + credi.camount
    print(sumcred)

    for debi in all1_debits :
        sumdeb=sumdeb + debi.damount
    print(sumdeb)

    balan=sumcred-sumdeb

    print(balan)
    return render(request, 'balance.html', {'balanc':balan})

def logout(request):
    auth.logout(request)
    return redirect("/")



