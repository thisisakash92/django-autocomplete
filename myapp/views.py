from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from haystack.query import SearchQuerySet
from myapp.models import SampleModel


def homepage(request):
    return render(request, 'base.html')


def my_search_view(request):
    #query haystack for 5 results
    sqs = SearchQuerySet().autocomplete(search_name=request.GET.get('q', ''))[:5]
    array = []
    for result in sqs:
        if isinstance(result.object, SampleModel):
            #check if the result is of the model we need
            #you only need this if you plan to index multiple models
            data = {
                "name": result.object.name,
                "url": result.object.get_absolute_url()
                }
            # add the filtered result to the array/list
            array.append(data)
    return JsonResponse(array, safe=False)
