from __future__ import unicode_literals
from django.db import models


class EC2Instance(models.Model):
    name = models.CharField(max_length=500)
    api_name = models.CharField(max_length=500)
    memory = models.FloatField(default=0) # in GiB
    vcpu = models.IntegerField(null=True, blank=True)
    instance_storage = models.TextField()
    network_performance = models.CharField(max_length=500, null=True, blank=True)
    linux_on_demand_cost = models.FloatField(default=0, null=True, blank=True)
    linux_reserved_cost = models.FloatField(default=0, null=True, blank=True)
    windows_on_demand_cost = models.FloatField(default=0, null=True, blank=True)
    windows_reserved_cost = models.FloatField(default=0, null=True, blank=True)


    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

    def get_dict(self):
        result = {}
        result['name'] = self.name if self.name else None
        result['api_name'] = self.api_name if self.api_name else None
        result['memory'] = self.memory if self.memory else None
        result['vcpu'] = self.vcpu if self.vcpu else None
        result['instance_storage'] = self.instance_storage if self.instance_storage else None
        result['network_performance'] = self.network_performance if self.network_performance else None
        result['linux_on_demand_cost'] = self.linux_on_demand_cost if self.linux_on_demand_cost else None
        result['linux_reserved_cost'] = self.linux_reserved_cost if self.linux_reserved_cost else None
        result['windows_on_demand_cost'] = self.windows_on_demand_cost if self.windows_on_demand_cost else None
        result['windows_reserved_cost'] = self.windows_reserved_cost if self.windows_reserved_cost else None
        return result
