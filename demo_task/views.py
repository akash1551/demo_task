import json
from .models import EC2Instance
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.db.models import Q


def filter_instance(request):
    if request.method == 'OPTIONS':
        return JsonResponse({'validation': 'Invalid request', 'status': True})

    params = json.loads(request.body.decode('utf-8'))
    print(params)
    network_performance = params.get('network_performance')
    search_string = params.get('search_string')
    memory = params.get('memory') if params.get('memory') else {}
    vcpu = params.get('vcpu') if params.get('vcpu') else {}
    linux_on_demand_cost = params.get('linux_on_demand_cost') if params.get('linux_on_demand_cost') else {}
    linux_reserved_cost = params.get('linux_reserved_cost') if params.get('linux_reserved_cost') else {}
    windows_on_demand_cost = params.get('windows_on_demand_cost') if params.get('windows_on_demand_cost') else {}
    windows_reserved_cost = params.get('windows_reserved_cost') if params.get('windows_reserved_cost') else {}
    kwargs = {}
    args = Q()

    if memory.get('start'):
        kwargs['memory__gte'] = float(memory.get('start'))
    if memory.get('end'):
        kwargs['memory__lte'] = float(memory.get('end'))

    if vcpu.get('start'):
        kwargs['vcpu__gte'] = float(vcpu.get('start'))
    if vcpu.get('end'):
        kwargs['vcpu__lte'] = float(vcpu.get('end'))

    if linux_on_demand_cost.get('start'):
        kwargs['linux_on_demand_cost__gte'] = float(linux_on_demand_cost.get('start'))
    if linux_on_demand_cost.get('end'):
        kwargs['linux_on_demand_cost__lte'] = float(linux_on_demand_cost.get('end'))

    if linux_reserved_cost.get('start'):
        kwargs['linux_reserved_cost__gte'] = float(linux_reserved_cost.get('start'))
    if linux_reserved_cost.get('end'):
        kwargs['linux_reserved_cost__lte'] = float(linux_reserved_cost.get('end'))

    if windows_on_demand_cost.get('start'):
        kwargs['windows_on_demand_cost__gte'] = float(windows_on_demand_cost.get('start'))
    if windows_on_demand_cost.get('end'):
        kwargs['windows_on_demand_cost__lte'] = float(windows_on_demand_cost.get('end'))

    if windows_reserved_cost.get('start'):
        kwargs['windows_reserved_cost__gte'] = float(windows_reserved_cost.get('start'))
    if windows_reserved_cost.get('end'):
        kwargs['windows_reserved_cost__lte'] = float(windows_reserved_cost.get('end'))

    if network_performance:
        kwargs['network_performance'] = network_performance

    if search_string:
        args = args | (Q(name__icontains=search_string) | \
            Q(api_name__icontains=search_string) | \
            Q(memory__icontains=search_string) | \
            Q(vcpu__icontains=search_string) | \
            Q(instance_storage__icontains=search_string) | \
            Q(network_performance__icontains=search_string) | \
            Q(linux_on_demand_cost__icontains=search_string) | \
            Q(linux_reserved_cost__icontains=search_string) | \
            Q(windows_on_demand_cost__icontains=search_string) | \
            Q(windows_reserved_cost__icontains=search_string))

    instances = EC2Instance.objects.filter(*(args,), **kwargs)
    data = [instance.get_dict() for instance in instances]
    # return render_to_response('html_templates/landing_page.html', {'data': data})
    return JsonResponse({'data': data, 'status': True})
