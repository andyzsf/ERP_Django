#!/usr/bin/python
#-*-coding:utf-8-*-

from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from engine.utils import get_datatables_records
from django.contrib.auth.decorators import login_required
from models import Class,Student,SEX_CHOICES, SUPERUSER_CHOISE
from django.utils import simplejson
from forms import StudentForm, UserForm
from django.utils.cache import add_never_cache_headers
import traceback
import time 
import datetime




from sql_ctrl import*
from myfunction import*

@login_required
def index(request):
    username = request.user.username

    #return render_to_response('student/student.html',{
    return render_to_response('user/user.html',{
            "title":'用户管理',
            'username':username},context_instance = RequestContext(request))

    
@login_required
def get_users_list(request):
    users = User.objects.filter()

    columnIndexNameMap = {
        0:'id',
        1:'username',
        2:'is_superuser',
        3:'email',
        4:'date_joined',
        5:'last_login',
    }
    
    columnNameIndexMap = dict([[v,k] for k,v in columnIndexNameMap.items()])
    
    updatefilter = {
        1:'username',
        2:'is_superuser',
    }
        
    extrafilters = {'is_superuser':SUPERUSER_CHOISE}
    
    updateitems = {
        1:'username',
        2:'is_superuser',
    }
    try:
        aaData,sEcho,iTotalRecords,iTotalDisplayRecords,sColumns = get_datatables_records(request,
                users, columnIndexNameMap,None,extrafilters,False,updatefilter,updateitems) 
    except Exception,e:
        traceback.print_stack()
        aaData,sEcho,iTotalRecords,iTotalDisplayRecords,sColumns = [],1,0,0,','.join(columnIndexNameMap.values())
     
    #for i in aaData:
        #i[columnNameIndexMap['message']] = User.objects.get( id = i[columnNameIndexMap['theclass']]).classid
        #i[columnNameIndexMap['is_superuser']] = dict(SUPERUSER_CHOISE)[i[columnNameIndexMap['is_superuser']]]
        #i[columnNameIndexMap['id']] = User.objects.get(id=i[columnNameIndexMap['id']]).username
        #i[columnNameIndexMap['theclass']] = Class.objects.get(id=i[columnNameIndexMap['theclass']]).classid

    response_dict = {}
    response_dict.update({'aaData':aaData})
    response_dict.update({
        'sEcho': sEcho, 
        'iTotalRecords': iTotalRecords, 
        'iTotalDisplayRecords':iTotalDisplayRecords, 
        'sColumns':sColumns})

    response =  HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')

    #阻止缓存
    add_never_cache_headers(response)
    return response


@login_required
def adduser(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            user_name = request.POST.get('username')
            user_power = 0
            user_power = request.POST.get('issuperuser')
            user_email = request.POST.get('useremail')
            
            time = datetime.datetime.now()
            timenow = time.strftime("%Y-%m-%d %H:%M:%S")
            try:
                sql = "INSERT INTO auth_user(username, email, is_superuser, first_name,last_name, password, is_staff, is_active, last_login, date_joined ) VALUES('%s','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s' )"%(
                        user_name, user_email, user_power,
                        '', '',
                        '111111',
                        1, 1,  
                        timenow, timenow)
                sql_one( sql )
                success = True
                successinfo = "新增用户"
                return render_to_response('user/user.html',{
                    "title":'用户管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except:
                error = "sql error"
                return render_to_response('error.html',locals())

        except:
            error = "get date error"
            return render_to_response('error.html',locals())

    return HttpResponseRedirect('/manage/user/')

@login_required
def edituser(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            user_id = request.POST.get('userid')
            user_name = request.POST.get('username')
            user_power = 0
            user_power = request.POST.get('issuperuser')
            user_email = request.POST.get('useremail')
            try:
                sql = "UPDATE auth_user SET username = '%s', is_superuser = '%s', email = '%s' where id = '%s' "%(user_name, 
                        user_power, user_email, user_id)
                sql_one( sql )
                success = True
                successinfo = "修改用户信息"
                return render_to_response('user/user.html',{
                    "title":'用户管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except User.DoesNotExist:
                traceback.print_stack()
        except Exception,e:
            traceback.print_stack()
            
    return HttpResponseRedirect('/manage/user/')


@login_required
def deleteuser(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            user_id = request.POST.get('id')
            try:
                sql = "DELETE FROM auth_user WHERE id = '%s'"%user_id
                sql_one( sql )
                success = True
                successinfo = "删除用户"
                return render_to_response('user/user.html',{
                    "title":'用户管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except User.DoesNotExist:
                traceback.print_stack()
        except Exception,e:
            traceback.print_stack()
        
    return HttpResponseRedirect('/manage/user/')



    
@login_required
def inituser(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            user_id = request.POST.get('id')
            try:
                #pwd = encrypt_password('111111')
                #sql_update( 'auth_user', user_id, 'password', pwd)
                inituser = User.objects.get(id = user_id)
                inituser.set_password('000000')
                inituser.save()
                success = True
                successinfo = "初始化密码"
                return render_to_response('user/user.html',{
                    "title":'用户管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except User.DoesNotExist:
                traceback.print_stack()
        except Exception,e:
            traceback.print_stack()
        
    return HttpResponseRedirect('/manage/user/')

@login_required
def userprofile(request):
    username = request.user.username
    student = request.user.student

    return render_to_response('user/profile.html',{
            "title":'同学详细信息',
            'studentid':username,
            'realname':student.realname,
            'sex':dict(SEX_CHOICES)[student.sex],
            'class':student.theclass.classid,
            'username':username},context_instance = RequestContext(request))
