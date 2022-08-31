import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    print(request.GET) # url query params
    body = request.body # byte string of json data
    data = {}
    try:
        data = json.loads(body) # string of json -> python dict
    except:
        pass
    # print(body)
    # return JsonResponse({"message": "Hi there, this is your Django Api response"})
    # print(data)
    # data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    # data['content_type'] = dict(request.content_type)
    print(type(data))
    return JsonResponse(data)