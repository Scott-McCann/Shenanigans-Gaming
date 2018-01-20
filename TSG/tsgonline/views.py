from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

# Create your views here.

def view_index(request):

    return render(request, 'tsgonline/index.html')
