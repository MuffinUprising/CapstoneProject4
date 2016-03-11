__author__ = 'casey'

import urllib.request
import urllib.parse
import json

def main():

    dpla_api = "cd25c210d8141e63e88e09634f6a37a7"
    # test_url = "http://api.dp.la/v2/items?q=food%20desert&api_key=cd25c210d8141e63e88e09634f6a37a7"
    # # test_values = {'q': 'food%20desert', 'api_key': dpla_api}
    #
    # # data = urllib.parse.urlencode(test_values)
    # # data = data.encode('utf-8')
    # request = urllib.request.Request(test_url)
    # response = urllib.request.urlopen(request)
    #
    # responseData = response.read()
    # print(responseData)

    try:
        url = "http://api.dp.la/v2/items?sourceResource.subject=%22food%20desert%22&fields=sourceResource.title,sourceResource.contributor,sourceResource.subject&callback=printResults&api_key=cd25c210d8141e63e88e09634f6a37a7"
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = str(resp.read())

        print(respData)
        printResults(respData, json)


    except Exception as e:
        print(str(e))

def printResults(respData, json):

    json = json.loads(respData)

    if "name" in json["subject"]:
        print(json["name"]["subject"])


if __name__ == '__main__':
    main()