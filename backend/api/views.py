import json
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict # usually used in django form
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializers


@api_view(["POST"])
# @api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):

    """
    DRF api view
    """

    # instance = Product.objects.all().order_by("?").first()
# HANDLING POST REQUEST START
    serializer = ProductSerializers(data=request.data)
    # print(serializer)
    # print("test")
    # print(type(serializer))
    # print("test")
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save() # This is the only way to create product serializer
        # print(serializer.data)
        # print("test")
        # data = serializer.data
        # print(type(data))
        return Response(serializer.data)
    return Response({"invalid": "not good data"})
# HANDLING POST REQUEST END

    # if instance:
    #     data = ProductSerializers(instance).data
        # data = model_to_dict(model_data, fields=['id','title'])
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # model instance (model_data)
        # turn a python dict
        # return JSON to my client
    # return Response(data)

    # request -> HttpRequest -> Django
    # print(request.GET) # url query params
    # body = request.body # byte string of json data
    # data = {}
    # try:
    #     data = json.loads(body) # string of json -> python dict
    # except:
    #     pass
    # # print(body)
    # # return JsonResponse({"message": "Hi there, this is your Django Api response"})
    # # print(data)
    # # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # # data['content_type'] = dict(request.content_type)
    # print(type(data))
    # return JsonResponse(data) #  this needs CSRF Cookie in case of POST request