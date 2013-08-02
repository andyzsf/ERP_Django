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

    return render_to_response('customer/customer.html',{
            "title":'客户管理',
            'username':username},context_instance = RequestContext(request))

    
@login_required
def get_customers_list(request):

    sql = "select * from customer where is_alive = '1'"

    customSearch = request.GET.get('sSearch', '').rstrip().decode('utf-8');
    #customSearch = request.GET.get('sSearch', '').rstrip().encode('utf-8');
    if customSearch != '':
        sql = sql + " and ( cust_id = '" + customSearch +"' or zipcode = '" + customSearch + "')"
        #sql = sql + " and cust_company like '" + customSearch + "%'"



    if int(request.GET.get("iSortCol_0")) == 0:
        if request.GET.get("sSortDir_0") == 'desc':
            sql = sql + " order by cust_id "
        else:
            sql = sql + " order by cust_id desc"
    if int(request.GET.get("iSortCol_0")) == 2:
        if request.GET.get("sSortDir_0") == 'desc':
            sql = sql + " order by cust_linkman "
        else:
            sql = sql + " order by cust_linkman desc"

    if int(request.GET.get("iSortCol_0")) == 4:
        if request.GET.get("sSortDir_0") == 'desc':
            sql = sql + " order by city "
        else:
            sql = sql + " order by city desc"

    if int(request.GET.get("iSortCol_0")) == 5:
        if request.GET.get("sSortDir_0") == 'desc':
            sql = sql + " order by region "
        else:
            sql = sql + " order by region desc"




    cursor = connection.cursor()
    cursor.execute(sql)
    fetchall = cursor.fetchall()


    rowcount = 0;
    aaData = []
    for obj in fetchall:
    	dic = []
    	for i in obj:
		    dic.append(i)
        aaData.append(dic)
        rowcount = rowcount + 1
    #for obj in fetchall:
        #dic = {}
        #dic['cust_id'] = obj[0]
        #dic['cust_company'] = obj[1]
        #dic['cust_linkman'] = obj[2]
        #dic['address'] = obj[3]
        #dic['city'] = obj[4]
        #dic['region'] = obj[5]
        #dic['zipcode'] = obj[6]
        #dic['tel'] = obj[7]
        #dic['fax'] = obj[8]
        #dic['homepage'] = obj[9]
        #dic['remark'] = obj[10]
        #aaData.append(dic)
        #rowcount = rowcount + 1


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
def addcustomer(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            company = request.POST.get('custcompany')
            address = request.POST.get('address')
            linkman = request.POST.get('linkman')
            city = request.POST.get('city')
            region = request.POST.get('region')
            zipcode = request.POST.get('zipcode')
            tel = request.POST.get('tel')
            fax = request.POST.get('fax')
            homepage = request.POST.get('homepage')
            remark = request.POST.get('message') 
            
            sql = "INSERT INTO customer ( cust_company, cust_linkman, address, city, region, zipcode, tel, fax, homepage, remark, is_alive) VALUES( '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s', '1') "%(
                    company, linkman, address, city, region, zipcode, tel, fax, homepage, remark )
            
            try:
                
                sql_one( sql )
                success = True
                successinfo = "新增用户"
                return render_to_response('customer/customer.html',{
                    "title":'用户管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except:
                error = "sql error: " +sql
                return render_to_response('error.html',locals())

        except:
            error = "get date error"
            return render_to_response('error.html',locals())

    return HttpResponseRedirect('/manage/customer/')

@login_required
def editcustomer(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            id = request.POST.get('custid')
            company = request.POST.get('custcompany')
            address = request.POST.get('address')
            linkman = request.POST.get('linkman')
            city = request.POST.get('city')
            region = request.POST.get('region')
            zipcode = request.POST.get('zipcode')
            tel = request.POST.get('tel')
            fax = request.POST.get('fax')
            homepage = request.POST.get('homepage')
            remark = request.POST.get('message')
            
            sql = "UPDATE customer SET cust_company = '%s', cust_linkman = '%s',address = '%s', city = '%s', region = '%s', zipcode = '%s', tel = '%s', fax = '%s', homepage = '%s', remark = '%s' where cust_id = '%s' "%(
                    company, linkman, address, city, region, zipcode, tel, fax, homepage, remark, id )
            try:
                sql_one( sql )
                success = True
                successinfo = "修改客户信息"
                return render_to_response('customer/customer.html',{
                    "title":'客户管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except :
                error = "sql error"
                return render_to_response('error.html',locals())
        except :
            error = "get date error"
            return render_to_response('error.html',locals())
            
    return HttpResponseRedirect('/manage/customer/')


@login_required
def deletecustomer(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            user_id = request.POST.get('custid')
            try:
                sql = "UPDATE customer SET is_alive = '0' WHERE cust_id = '%s'"%user_id
                sql_one( sql )
                success = True
                successinfo = "注销客户"
                return render_to_response('customer/customer.html',{
                    "title":'客户管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except :
                error = "sql error" + sql
                return render_to_response('error.html',locals())
        except :
            error = "get date error"
            return render_to_response('error.html',locals())
        
    return HttpResponseRedirect('/manage/customer/')


