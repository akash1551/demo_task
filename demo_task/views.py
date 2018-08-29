from .models import EC2Instance
from django.http import JsonResponse
from django.shortcuts import render_to_response

def get_all_locations(request):
    locations = EC2Instance.objects.all()
    data = [item.get_dict() for item in locations]
    return render_to_response('html_templates/landing_page.html', {'data': data})
    # return JsonResponse({'data': data, 'status': True})

def landing_page(request):
    return render_to_response('html_templates/landing_page.html')
