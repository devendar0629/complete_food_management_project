from django.shortcuts import render,redirect

from .models import User

from hotelDetailsApp.models import HotelDetails

from hotelDetailsApp.forms import HotelDetailsForm

# Create your views here.
def show_user(request,username):
    if(request.GET.get('q','') is not None):
        query = request.GET.get('q','')
        context = {
            'userData':[],
            'username':username
        }
        queryLength = len(query)
        query = query[:queryLength-1]

        relatedData = HotelDetails.objects.filter(name__startswith = query)

        for data in relatedData:
            context['userData'].append(data)

        return render(request,'user/loggedInUser.html',context)

    context = {
        'userData':[],
        'username':username
    }
    for data in HotelDetails.objects.filter(username = User.objects.get(username = username)):
        context['userData'].append(data)

    return render(request,'user/loggedInUser.html',context)


def filter_type(request,type:str,**kwargs):
    data = HotelDetails.objects.filter(type = type)
    if(type == 'hotels'):
        data = HotelDetails.objects.filter(type = 'hotel')
    elif(type == 'trusts'):
        data = HotelDetails.objects.filter(type = 'trust')
    elif(type == 'refugeecamps'):
        data = HotelDetails.objects.filter(type = 'refugee_camp')

    if(data.exists()):
        return render(request,'user/loggedInUser.html',{'userData':data,'username':kwargs['username']})
    else:
        return render(request,'user/loggedInUser.html',{'username':kwargs['username']})

def hotel_details_form(request,username):
    form = HotelDetailsForm()
    if(request.method == 'POST'):
        form = HotelDetailsForm(request.POST)
        if(form.is_valid()):
            foodAvailability = request.POST.get('foodAvailability')
            print('Food availability : ',foodAvailability)
            if(foodAvailability is None):
                foodAvailability = False
            else:
                foodAvailability = True

            HotelDetails.objects.create(
                name = request.POST.get('name'),
                place = request.POST.get('place'),
                foodAvailability = foodAvailability,
                quantity = request.POST.get('quantity'),
                contactNumber = request.POST.get('contactNumber'),
                foodVarieties = request.POST.get('foodVarieties'),
                imagePath = request.POST.get('imagePath'),
                type = request.POST.get('type'),
                username = User.objects.get(username = username)
            )

            # print(User.objects.get(username = username))

            url = f'home/{username}'
            # print(type(request.POST.get('foodAvailability')))
            return redirect('/' + url + '/')
    context = {
        'form':form
    }
    return render(request,'hotelDetails/hotelDetailsForm.html',context)