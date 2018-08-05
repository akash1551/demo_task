from .models import CultureAndRecreation
from django.http import JsonResponse
from django.shortcuts import render_to_response

def get_all_locations(request):
    locations = CultureAndRecreation.objects.all()
    data = [item.location for item in locations]
    return JsonResponse({'data': data, 'status': True})

def landing_page(request):
    return render_to_response('html_templates/map_search.html')
