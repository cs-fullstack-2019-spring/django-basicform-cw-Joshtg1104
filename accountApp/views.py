from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Account


# Create your views here.
def index(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }
    return render(request, 'accountApp/index.html', context)


def helloMate(request):
    print(request.POST)
    print(request.POST["personName"])
    return HttpResponse("Welcome to " + request.POST["personName"] + "'s Account")


def add5Dollars(request, accountID):
    separateAccount = get_object_or_404(Account, pk=accountID)
    separateAccount.checking += 5
    separateAccount.save()

    accounts = Account.objects.all()

    context = {
        "accounts": accounts
    }

    return render(request, 'accountApp/index.html', context)
