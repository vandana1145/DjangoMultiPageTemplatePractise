from django.shortcuts import render
from .forms import babySitterForm

# Create your views here.

def index(req):
    return render(req, 'index.html')


def babysitters(req):
    return render (req, 'babysitters.html')


def contact(req):
    form = babySitterForm()
    if req.method == 'POST':
        form = babySitterForm(req.POST)
        if form.is_valid():
            form.save()
            print('saved')
            
    context = {
        'form' : form,
    }
    return render(req, 'contact.html', context)

    # render(req, kaha dikhana hai, kya leke jana hai)


def gallery(req):
    return render(req, 'gallery.html')


def parents(req):
    return render(req, 'parents.html')


def singlepage(req):
    return render(req, 'singlepage.html')


def typo(req):
    return render(req, 'typo.html')