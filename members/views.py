from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import MemberForm
from .models import Member


def members(request):
  form = MemberForm()

  if request.method == 'POST':
    form = MemberForm(request.POST)
    if form.is_valid():
      form.save()

  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
    'form': form,
  }
  return HttpResponse(template.render(context, request))


def myfirst(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def profile(request):
  template = loader.get_template('profile.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def alifmobile(request):
  template = loader.get_template('alifmobile.html')
  return HttpResponse(template.render())

def alifonline(request):
  template = loader.get_template('alifonline.html')
  return HttpResponse(template.render())

def alifshop(request):
  template = loader.get_template('alifshop.html')
  return HttpResponse(template.render())

def carfinance(request):
  template = loader.get_template('carfinance.html')
  return HttpResponse(template.render())

def deposits(request):
  template = loader.get_template('deposits.html')
  return HttpResponse(template.render())

def salam(request):
  template = loader.get_template('salam.html')
  return HttpResponse(template.render())

def transfers(request):
  template = loader.get_template('transfers.html')
  return HttpResponse(template.render())

def visa(request):
  template = loader.get_template('visa.html')
  return HttpResponse(template.render())


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())







# def members(request):
#     return HttpResponse("This team Yaqoob, Ahmad, Mahmud, Kalbi, Jan Aga,")


# def yaqoob(request):
#     return HttpResponse("Hello This is Yaqoob Team, Ahmad, Mahmud, Kalbi, Jan Aga,")


# def ahmad(request):
#     return HttpResponse("hello this is Ahmad")

# def kalbi(request):
#     return HttpResponse("Hello this is Kalbi")

# def mahmod(request):
#     return HttpResponse("hello this is Mahmod")



# Create your views here.
