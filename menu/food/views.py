from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from . import forms
from . import models


# Create your views here.
# def index(request):
#     item_list = models.Item.objects.all()
#     template: any = loader.get_template('item.html')
#     context = {
#         'item_list': item_list
#     }
#     return HttpResponse(template.render(context, request))
# return render(request, 'item.html', context={'item_list': item_list})

class IndexClassView(ListView):
    model = models.Item
    print(model)
    template_name = 'item.html'
    context_object_name = 'item_list'


def details(request, item_id):
    item_detail = models.Item.objects.get(pk=item_id)
    return render(request, 'details.html', context={'item_detail': item_detail})


class FoodDetails(DetailView):
    model = models.Item
    template_name = 'details.html'


def create_item(request):
    form = forms.ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'form.html', context={'form': form})


# class base create item

class CreateItem(CreateView):
    model = models.Item;
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

def update_item(request, item_id):
    item = models.Item.objects.get(id=int(item_id))
    form = forms.ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'form.html', context={'form': form, 'item': item})


def delete_item(request, item_id):
    item = models.Item.objects.get(pk=int(item_id))
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'item_delete.html', context={'item': item})
