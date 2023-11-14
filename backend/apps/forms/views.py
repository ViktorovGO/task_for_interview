from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .validation import validation


@csrf_exempt
def get_form(request):

    if request.method == 'POST':
        data=dict(request.POST)
        find_match = find_template(data)
 
        if find_match:
            return JsonResponse({'name':find_match})
        else:
            return JsonResponse({k:validation(data[k][0], field_type='text', out_type=True) for k,v in data.items()})
                
    return JsonResponse({'name':'Ничего'})


def find_template(data):

    for temp in sorted(MyForm.objects.all(), key=lambda x: len([i for i,v in x.__dict__.items() if v!=None]), reverse=True):
        inp_set = set(data)
        temp_set = [v for v in set(temp.__dict__.keys())- {'id','_state','name'} if temp.__dict__[v]!=None]
        keys = list(inp_set.intersection(temp_set))

        if set(data).issuperset(temp_set):
            if all([validation(data[k][0], temp.__dict__[k]) for k in keys]):
                return temp.name
            return False
    return False

