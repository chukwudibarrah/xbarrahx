from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateAccountForm

# Create registration session
def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateAccountForm()
    context = {
        'form': form,
    }
    return render(request, 'users/create_account.html', context)

def my_account(request):
    return render(request, 'users/my_account.html')