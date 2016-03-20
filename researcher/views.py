from django.shortcuts import render
from .models import DplaResult, Researcher, Images, Wiki
import urllib.request
import urllib.parse
from django.utils import timezone
import json
import wikipedia

#CONTROLLERS
dpla_api = "cd25c210d8141e63e88e09634f6a37a7"


def researcher(request):
    research = Researcher.objects.all()
    return render(request, 'search/researcher.html', {'research': research})


def search_dpla(user_query):

    try:
        # user_query = "food+AND+desert"
        return_fields = "isShownAt," \
                        "sourceResource.title," \
                        "sourceResource.contributor," \
                        "sourceResource.subject," \
                        "sourceResource.description," \
                        "sourceResource.date.begin," \
                        "provider.name"
        url = "http://api.dp.la/v2/items?sourceResource.subject="+user_query+"&page_size=5&fields="+return_fields+"&api_key="+dpla_api
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        resp_data = str(resp.read())

        print(resp_data)


    except Exception as e:
        print(str(e))


def verify_json(request):
    try:
        request.json()

    except ValueError as e:
        return "Error: {}".format(e)

    return request

def create_dpla_result(resp_data):
    response_dict = resp_data.get('response')
    dpla_result = DplaResult(
        url=response_dict.get('isShownAt'),
        subject_heading1=response_dict.get('sourceResource.subject'),
        subject_heading2=response_dict.get('sourceResource.subject'),
        subject_heading3=response_dict.get('sourceResource.subject'),
        summary=response_dict.get('sourceResource.description'),
        author=response_dict.get('sourceResource.contributor'),
        publisher=response_dict.get('provider.name'),
        date_published=response_dict.get('sourceResource.date.begin')
    )
    print(str(dpla_result))
    return dpla_result