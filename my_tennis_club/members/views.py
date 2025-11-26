from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
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

def testing(request):
  template = loader.get_template('template.html')
  mymembers = Member.objects.all().values()
  column_firstname = Member.objects.values_list("firstname")
  records_Carlos = Member.objects.filter(firstname__exact="Carlos").values()
  colum_range = Member.objects.filter(id__range=(2, 4)).values()
  busquer_id = Member.objects.filter(id__lte=3).values()
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
    'mymembers': mymembers,
    'column_firstname': column_firstname,
    'records_Felipe': records_Carlos,
    'colum_range': colum_range,
    'busquer_id': busquer_id,
  }
  return HttpResponse(template.render(context, request))