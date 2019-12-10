from django.shortcuts import render
from django.http import HttpResponse


def predict(request):
    values = {"res": "150|160|170|180|190|200|210"}
    if request.method == 'POST':
        city = request.POST.get('city')
        # zip_code = request.POST.get('zip-code')
        # property_type = request.POST.get('property-type')
        # room_type = request.POST.get('room-type')
        # bed_type = request.POST.get('bed-type')
        # minimum_nights = request.POST.get('minimum-nights')
        # bedroom_num = request.POST.get('bedroom-num')
        # bed_num = request.POST.get('bed-num')
        # bathroom_num = request.POST.get('bathroom-num')
        values["res"] = "210|200|190|180|170|160|150"
        return render(request, 'predictor.html', values)
        
    return render(request, 'predictor.html', values)
