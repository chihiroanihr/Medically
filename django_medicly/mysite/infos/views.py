from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .forms import UserInputForm


def add_user(request):
    if request.method == 'POST':  # data sent by user
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()  # this will save Car info to database
            return HttpResponse('UserInput added to database')
    else:  # display empty form
        form = UserInputForm()

    return render(request, 'add_user.html', {'form': form})

def user_list(request):
    return render(request, 'user_list.html', {
        # this will fetch all cars from database
        'users': UserInput.objects.all()
    })
