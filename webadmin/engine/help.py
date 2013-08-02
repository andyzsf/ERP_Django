#!/usr/bin/python
#-*-coding:utf-8-*-

from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from engine.utils import get_datatables_records
from django.contrib.auth.decorators import login_required
from models import SUPERUSER_CHOISE
from django.utils import simplejson
from forms import UserForm
from django.utils.cache import add_never_cache_headers
import traceback
import time 
import datetime




from django.db import connection, transaction
from sql_ctrl import*

@login_required
def index(request):
    username = request.user.username

    return render_to_response('help/help.html',{
            "title":'帮助,
            'username':username},context_instance = RequestContext(request))


    




