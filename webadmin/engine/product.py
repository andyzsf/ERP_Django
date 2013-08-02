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

    return render_to_response('product/product.html',{
            "title":'产品管理',
            'username':username},context_instance = RequestContext(request))

    
@login_required
def get_products_list(request):
    rawsql = "select * from product where is_alive = '1'"

    customSearch = request.GET.get('sSearch', '').rstrip().encode('utf-8');
    #if customSearch != '':
    #    rawsql = rawsql + " where address like '%" + customSearch + "%'"



    if int(request.GET.get("iSortCol_0")) == 0:
        if request.GET.get("sSortDir_0") == 'desc':
            sql = rawsql + " order by product_id "
        else:
            sql = rawsql + " order by product_id desc"



    cursor = connection.cursor()
    cursor.execute(rawsql)
    fetchall = cursor.fetchall()


    rowcount = 0;
    aaData = []
    for obj in fetchall:
    	dic = []
    	for i in obj:
		    dic.append(i)
        aaData.append(dic)
        rowcount = rowcount + 1
    

    cols = int(request.GET.get('iColumns',0)) #获取有多少列数据
    iDisplayLength = min(int(request.GET.get('iDisplayLength',10)),100)     #每页获取rows个数
    startRecord = int(request.GET.get('iDisplayStart',0)) #本页第一条数据，是所有数据的第几个,从0开始
    endRecord = startRecord + iDisplayLength 
    sEcho = int(request.GET.get('sEcho',0)) #页数
    
    #iTotalRecords = iTotalDisplayRecords = grades.count() #总共的rows数
    iTotalRecords = iTotalDisplayRecords = rowcount #总共的rows数
    aaData = aaData[startRecord:endRecord]
    #grades = grades[startRecord:endRecord]

    #aaData = [[unicode(i.term),unicode(i.student.realname),unicode(i.student.user.username),unicode(i.student.theclass.classid),unicode(str(i.score)),] for i in grades]

    response_dict = {}
    response_dict.update({'aaData':aaData})
    response_dict.update({
        'sEcho': sEcho, 
        'iTotalRecords': iTotalRecords, 
        'iTotalDisplayRecords':iTotalDisplayRecords})

    response =  HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')

    #阻止缓存
    add_never_cache_headers(response)
    return response


@login_required
def addproduct(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            id = request.POST.get('id')
            productname = request.POST.get('productname')
            productspec = request.POST.get('productspec')
            unit = request.POST.get('unit')
            message = request.POST.get('message')
            
            sql = "INSERT INTO product( product_name, spec, unit, remark) VALUES ( '%s', '%s', '%s','%s' )"%(
                        productname, productspec, unit, message )
            try:
                sql_one( sql )
                success = True
                successinfo = "新增用户"
                return render_to_response('product/product.html',{
                    "title":'用户管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except:
                error = "sql error" + sql
                return render_to_response('error.html',locals())

        except:
            error = "get date error"
            return render_to_response('error.html',locals())

    return HttpResponseRedirect('/manage/product/')

@login_required
def editproduct(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            id = request.POST.get('id')
            productname = request.POST.get('productname')
            productspec = request.POST.get('productspec')
            unit = request.POST.get('unit')
            message = request.POST.get('message')
            
            sql = "UPDATE product SET product_name = '%s',spec = '%s', unit = '%s', remark = '%s' where product_id = '%s' "%(
                        productname, productspec, unit, message, id)
            try:
                sql_one( sql )
                success = True
                successinfo = "修改产品信息"
                return render_to_response('product/product.html',{
                    "title":'产品管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except :
                error = "sql error" + sql
                return render_to_response('error.html',locals())
        except :
            error = "get date error: "+ message
            return render_to_response('error.html',locals())
            
    return HttpResponseRedirect('/manage/product/')


@login_required
def deleteproduct(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            id = request.POST.get('id')
            try:
                sql = "UPDATE product SET is_alive = '0' WHERE product_id = '%s'"%id
                sql_one( sql )
                success = True
                successinfo = "注销产品"
                return render_to_response('product/product.html',{
                    "title":'产品管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except User.DoesNotExist:
                traceback.print_stack()
        except Exception,e:
            traceback.print_stack()
        
    return HttpResponseRedirect('/manage/product/')



    

