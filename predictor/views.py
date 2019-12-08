from django.shortcuts import render
from django.http import HttpResponse

def predict(request):
    # context = {}
    if request.method == 'POST':
        pass
        # custom_fields = []
        # custom_fields.append({'sign_date': request.POST.get('sign_date', '')})
        # custom_fields.append({'old_policy_end_date': request.POST.get('end_date', '')})
        # custom_fields.append({'old_insurer': request.POST.get('old_insurer', '')})
        # custom_fields.append({'new_policy_start_date': request.POST.get('start_date', '')})
        # custom_fields.append({'policy_descriptions': request.POST.get('policy_descriptions', '')})
        # custom_fields.append({'address1': request.POST.get('address1', '')})
        # custom_fields.append({'address2': request.POST.get('address2', '')})
        # email_address = request.POST.get('email_address', '')
        # first_name = request.POST.get('first_name', '')
        # last_name = request.POST.get('last_name', '')
        # custom_fields.append({'name': first_name + ' ' + last_name})
        # send_request_with_template(custom_fields, email_address, first_name)
        # context["succeed"] = True
    return render(request, 'predictor.html')
