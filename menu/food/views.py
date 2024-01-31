from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import  loader
from . import models
from . import forms
# Create your views here.
def index(request):
    item_list = models.Item.objects.all()
    print(item_list[1].item_price)
    template: any = loader.get_template('item.html')
    context = {
        'item_list': item_list
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'item.html', context={'item_list': item_list})

def details(request, item_id):
    item_detail = models.Item.objects.get(pk=item_id)
    return render(request, 'details.html', context={'item_detail': item_detail})

def create_item(request):

    form = forms.ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'form.html', context={'form': form})