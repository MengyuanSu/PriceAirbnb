from django.shortcuts import render
from django.http import HttpResponse

def predict(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        zip_code = request.POST.get('zip-code')
        property_type = request.POST.get('property-type')
        room_type = request.POST.get('room-type')
        bed_type = request.POST.get('bed-type')
        minimum_nights = request.POST.get('minimum-nights')
        bedroom_num = request.POST.get('bedroom-num')
        bed_num = request.POST.get('bed-num')
        bathroom_num = request.POST.get('bathroom-num')
        
    return render(request, 'predictor.html')
