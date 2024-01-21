from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from user.models import User
from hotelDetailsApp.models import HotelDetails

from loginApp.views import show_login_form

def show_base(request):
    allData = HotelDetails.objects.all()
    context = {
        'allData':allData
    }
    return render(request,'base/base.html',context)

def filter_type(request,type:str,**kwargs):
    data = HotelDetails.objects.filter(type = type)
    if(type == 'hotels'):
        data = HotelDetails.objects.filter(type = 'hotel')
    elif(type == 'trusts'):
        data = HotelDetails.objects.filter(type = 'trust')
    elif(type == 'refugeecamps'):
        data = HotelDetails.objects.filter(type = 'refugee_camp')

    if(data.exists()):
        return render(request,'base/base.html',{'allData':data})
    else:
        return render(request,'base/base.html',{})

def search_view(request):
    places = HotelDetails.objects.all()
    query = request.GET.get('q','')
    print('search view')
    context = {
        'allData':[]
    }

    for place in places:
        if(place.name.__contains__(query)):
            context.get('allData').append(place)

    return render(request,'base/base.html',context)