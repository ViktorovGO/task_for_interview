from .validation import validation
from .models import MyForm

def find_template(data: dict[str, list[str]]):

    inp_set = set({k:validation(v[0]) for k,v in data.items()}.items())
    """Получаем set с элементами вида ('field_name','field_type'), тип определяется на основе валидации"""

    for form in sorted(MyForm.objects.all(), key=lambda x: len([i for i,v in x.__dict__.items() if v!=None]), reverse=True):
        pos_form = {v:k for k,v in form.__dict__.items() if v!=None and k not in {'id','_state','name'}}
        pos_form_set = set(pos_form.items()) # set с полями из шаблона формы в формате ('field_name','field_type')
        if inp_set.issuperset(pos_form_set): # Проверяем что pos_form_set является подмножеством inp_set
            return form.name

    return False