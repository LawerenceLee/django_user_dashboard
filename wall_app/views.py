# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib import messages
def index(request):
    return render(request, 'wall_app/index.html')
