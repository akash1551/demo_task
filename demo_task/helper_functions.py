import pandas as pd
from demo_task.models import CultureAndRecreation
from django.db import transaction
from bs4 import BeautifulSoup


def create_culture_and_recreation(filepath):
    df = pd.read_csv(filepath)
    df.columns = ['title', 'release_year', 'location', 'fun_fact',
                  'production_company', 'distributor', 'director', 'writer',
                  'actor1', 'actor2', 'actor3']

    values = df.T.to_dict().values()
    print('values: ', values)
    data = [CultureAndRecreation(title=val['title'], release_year=val['release_year'],
                                  location=val['location'], fun_fact=val['fun_fact'],
                                  production_company=val['production_company'], distributor=val['distributor'],
                                  director=val['director'], writer=val['writer'], actor1=val['actor1'],
                                  actor2=val['actor2'], actor3=val['actor3']) for val in values]
    with transaction.atomic():
        CultureAndRecreation.objects.bulk_create(data)

    return True
