from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .validation import validation
from .utils import  find_template

@csrf_exempt
def get_form(request):

    if request.method == 'POST':
        # print(request.POST)
        data = dict(request.POST)
        find_match = find_template(data)
 
        if find_match:
            return JsonResponse({'name':find_match})
        else:
            return JsonResponse({k:validation(v[0]) for k,v in data.items()})
                
    # return JsonResponse({'name':''})
    return HttpResponse(status=401)




