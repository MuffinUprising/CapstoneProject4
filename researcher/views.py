from django.shortcuts import render, get_object_or_404
from .models import DplaResult, Researcher, Images, Wiki
import urllib.request
import urllib.parse
from django.utils import timezone
import json
import wikipedia

#CONTROLLERS (note to self)
# dpla api key
dpla_api = "cd25c210d8141e63e88e09634f6a37a7"

# front page
def researcher(request):
    research = Researcher.objects.all()
    return render(request, 'search/researcher.html', {'research': research})

#previous searches
def search_previous(request, pk):
    search = get_object_or_404(Researcher, pk=pk)
    return render(request, 'search/search_detail.html', {'search': search})


# DPLA query
def search_dpla(user_query):

    try:
        # user_query = "food+AND+desert"

        # fields to return from API call
        return_fields = "isShownAt," \
                        "sourceResource.title," \
                        "sourceResource.contributor," \
                        "sourceResource.subject," \
                        "sourceResource.description," \
                        "sourceResource.date.begin," \
                        "provider.name"
        #URL for call
        url = "http://api.dp.la/v2/items?sourceResource.subject="+user_query+"&page_size=5&fields="+return_fields+"&api_key="+dpla_api
        # request/response
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        #decode and load json file
        resp_data = resp.read().decode("UTF-8")
        json_resp = json.loads(resp_data)
        # json_data = json_resp['data']

        #test print
        print(str(json_resp))
        return json_resp


    except Exception as e:
        print(str(e))

# yet unimplemented
def verify_json(request):
    try:
        request.json()

    except ValueError as e:
        return "Error: {}".format(e)

    return request

# set dpla_result attributes
def create_dpla_result(q):
    response_dict = q.get('response')  # <-- response not getting passed here
    print("response dict: " + str(response_dict))
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

# search detail
def search_detail(request):
    user_query = request.GET.get('user_query')
    print("Query: " + user_query)
    q = search_dpla(user_query)
    print("Result: " + str(q))  # results are here
    new_query = create_dpla_result(q)
    print(new_query)
    return render(request, 'search/search_detail', {'dpla': new_query})