from django.shortcuts import render,redirect
# from django.http import HttpResponseRedirect

from .forms import HotelDetailsForm
from .models import HotelDetails
from user.models import User

# # Create your views here.
# def hotel_details_form(request):
#     print("FORM")
#     form = HotelDetailsForm()
#     if(request.method == 'POST'):
#         form = HotelDetailsForm(request.POST)
#         if(form.is_valid()):
#             # foodAvailability = request.POST.get('foodAvailability')
#             foodAvailability = True
#             if(foodAvailability is None):
#                 foodAvailability = False
#             else:
#                 foodAvailability = True

#             # HotelDetails.objects.create(
#             #     name = request.POST.get('name'),
#             #     place = request.POST.get('place'),
#             #     foodAvailability = foodAvailability,
#             #     quantity = request.POST.get('quantity'),
#             #     contactNumber = request.POST.get('contactNumber'),
#             #     foodVarieties = request.POST.get('foodVarieties'),
#             #     imagePath = request.POST.get('imagePath'),
#             #     type = request.POST.get('type'),
#             #     username = User.objects.get(username = username)
#             # )

#             # print(User.objects.get(username = username))

#             # url = f'home/{username}'
#             # # print(type(request.POST.get('foodAvailability')))
#             # return redirect('/' + url + '/')
#     context = {
#         'form':form
#     }
#     return render(request,'hotelDetails/hotelDetailsForm.html',context)