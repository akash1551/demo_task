from .models import CultureAndRecreation
from django.http import JsonResponse
from django.shortcuts import render_to_response

def get_all_locations(request):
    locations = CultureAndRecreation.objects.all()
    data = [item.get_dict() for item in locations]
    return render_to_response('html_templates/landing_page.html', {'data': data})
    # return JsonResponse({'data': data, 'status': True})

def landing_page(request):
    return render_to_response('html_templates/landing_page.html')
