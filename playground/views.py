from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, Min, Max, Avg, Sum
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist

from store.models import Order, Product, Customer, Collection, Promotion

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Kkk', 'result': list()})