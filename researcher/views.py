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
                        "sourceResource.creator," \
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
    response_dict = q.get('docs')
    #iterate over list
    dpla_results = []

    for item in response_dict:
        # list comprehension - Thanks to Boyd!
        sh_list = [i.get('name') for i in item.get('sourceResource.subject')]
        sh_dict = {'subject_heading' + str(i+1): u for i, u in enumerate(sh_list)}
        # perform .get
        dpla_result = DplaResult(
            url=item.get('isShownAt'),
            summary=item.get('sourceResource.description'),
            author=item.get('sourceResource.creator'),
            publisher=item.get('provider.name'),
            date_published=item.get('sourceResource.date.begin'),
            **sh_dict
        )
        dpla_results.append(dpla_result)

    return dpla_results

# search detail
def search_detail(request):
    user_query = request.GET.get('user_query')
    print('Query:' + user_query)
    q = search_dpla(user_query)
    dpla_query = create_dpla_result(q)
    wiki = search_wikipedia(user_query)
    images = search_wikimedia(user_query)

    return render(request, 'search/search_detail.html', {'dpla_results': dpla_query,
                                                         'wiki_result': wiki,
                                                         'image_results': images})


def search_wikipedia(request):
    result = wikipedia.page(request)
    wiki_url = result.url
    wiki_title = result.title
    wiki_summary = result.summary
    wiki = Wiki(url=wiki_url, title=wiki_title, summary=wiki_summary)

    return wiki

def search_wikimedia(request):
    page = wikipedia.page(request)
    image_url_list = []
    print("Number of images on page: " + str(len(page.images)))
    if len(page.images) < 5:
        number_to_display = len(page.images)
    else:
        number_to_display = 5
    i = 0
    while i < number_to_display:
        image_url_list.append(page.images[i])
        i += 1
    print(image_url_list)
    image_dict = {'imageURL' + str(i+1): u for i, u in enumerate(image_url_list)}
    print(str(image_dict))
    images = Images(**image_dict)

    return images



def create_images_result(q):
    pass

