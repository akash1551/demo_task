import pandas as pd
from demo_task.models import EC2Instance
from django.db import transaction
from bs4 import BeautifulSoup
import urllib.request
import re


TARGET_URL = 'https://www.ec2instances.info/'


def create_ec2instance_data():
    print("Connecting to: {}".format(TARGET_URL))
    root_page = urllib.request.urlopen(TARGET_URL).read()
    print("Connection established")
    soup = BeautifulSoup(root_page, 'lxml')
    table = soup.find('table', {'id': 'data'})
    df_table = pd.read_html(root_page)[0]
    new_df = df_table[['Name', 'API Name', 'Memory', 'vCPUs', 'Instance Storage',
                       'Network Performance', 'Linux On Demand cost', 'Linux Reserved cost',
                       'Windows On Demand cost', 'Windows Reserved cost']].copy()
    print('new_df: ', new_df)
    bulk_insert_instances(new_df)


def bulk_insert_instances(df):
    df.columns = ['name', 'api_name', 'memory', 'vcpu',
                  'instance_storage', 'network_performance',
                  'linux_on_demand_cost', 'linux_reserved_cost',
                  'windows_on_demand_cost', 'windows_reserved_cost']

    values = df.T.to_dict().values()
    print('values: ', values)
    data = [EC2Instance(name=val['name'],
                                 api_name=val['api_name'],
                                 memory=float(val['memory'].split(' ')[0]),
                                 vcpu=int(val['vcpu'].split(' ')[0]) if val['vcpu'].split(' ')[0] != 'N/A' else None,
                                 instance_storage=val['instance_storage'],
                                 network_performance=val['network_performance'],
                                 linux_on_demand_cost=re.findall("\d+\.\d+", val['linux_on_demand_cost'])[0] if len(re.findall("\d+\.\d+", val['linux_on_demand_cost'])) > 0 else None,
                                 linux_reserved_cost=re.findall("\d+\.\d+", val['linux_reserved_cost'])[0] if len(re.findall("\d+\.\d+", val['linux_reserved_cost'])) > 0 else None,
                                 windows_on_demand_cost=re.findall("\d+\.\d+", val['windows_on_demand_cost'])[0] if len(re.findall("\d+\.\d+", val['windows_on_demand_cost'])) > 0 else None,
                                 windows_reserved_cost=re.findall("\d+\.\d+", val['windows_reserved_cost'])[0] if len(re.findall("\d+\.\d+", val['windows_reserved_cost'])) > 0 else None) for val in values]
    with transaction.atomic():
        EC2Instance.objects.bulk_create(data)

    return True
