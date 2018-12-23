from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import FSentence

# Create your views here.
def index(request):

    fklist = FSentence.objects.order_by('sub_date')[:2]
    fklist = [a.orig_text for a in fklist]
    print(fklist)
    output = json.dumps(fklist)
    return HttpResponse(output)
