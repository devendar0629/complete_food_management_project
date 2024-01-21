from django import forms

class HotelDetailsForm(forms.Form):
    name = forms.CharField(max_length = 40)
    place = forms.CharField(max_length = 50)
    foodAvailability = forms.BooleanField(widget = forms.CheckboxInput,required=False)
    quantity = forms.IntegerField(min_value=0)
    contactNumber = forms.IntegerField(max_value=9999999999,min_value=1000000000)
    foodVarieties = forms.CharField(widget=forms.TextInput)
    imagePath = forms.CharField(widget=forms.TextInput)
    type = forms.ChoiceField(choices=(('hotel','Hotel'),('trust','Trust'),('refugee_camp','Refugee Camp')))