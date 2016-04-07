from django.shortcuts import render, redirect
from apps.ninja_gold.models import Wallet, Form


# Create your views here.

def index(request):
    wallet = Wallet(request)
    context = {
        'total': wallet.total_gold,
        'activites': wallet.activites
    }
    return render(request, 'ninja/index.html', context)


def find_gold(request):
    if request.method == 'POST':
        wallet = Wallet(request)
        form = Form(request.POST)
        if form.is_valid():
            wallet.find_gold(form.cleaned_data['ninja'])
    return redirect('/')
