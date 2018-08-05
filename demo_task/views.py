from .models import CultureAndRecreation
from django.http import JsonResponse


def get_all_locations(request):
    locations = CultureAndRecreation.objects.all()
    data = [item.location for item in locations]
    return JsonResponse({'data': data, 'status': True})
