from .models import EC2Instance
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.db.models import Q


def filter_instance(request):
    params = json.loads(request.body.decode('utf-8'))
    search_string = params.get('search_string')
    memory = params.get('memory')
    vcpu = params.get('vcpu')
    instance_storage = params.get('instance_storage')
    network_performance = params.get('network_performance')
    kwargs = {}
    args = Q()

    if memory:
        kwargs['memory'] = memory

    if vcpu:
        kwargs['vcpu'] = vcpu

    if instance_storage:
        kwargs['instance_storage'] = instance_storage

    if network_performance:
        kwargs['network_performance'] = network_performance

    if search_string:
        args = args | (Q(name__icontains=search_string) | \
            Q(api_name__icontains=search_string) | \
            Q(memory__icontains=search_string) | \
            Q(vcpu__icontains=search_string) | \
            Q(internal_storage__icontains=search_string) | \
            Q(network_performance__icontains=search_string) | \
            Q(linux_on_demand_cost__icontains=search_string) | \
            Q(linux_reserved_cost__icontains=search_string) | \
            Q(windows_on_demand_cost__icontains=search_string) | \
            Q(windows_reserved_cost__icontains=search_string))

    instances = EC2Instance.objects.filter(*(args,), **kwargs)
    data = [item.get_dict() for item in locations]
    return render_to_response('html_templates/landing_page.html', {'data': data})
    # return JsonResponse({'data': data, 'status': True})

def landing_page(request):
    return render_to_response('html_templates/landing_page.html')
