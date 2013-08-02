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

    return render_to_response('sale/sale.html',{
            "title":'销售管理',
            'username':username},context_instance = RequestContext(request))


    
@login_required
def get_sales_list(request):
    rawsql = "select s.sell_id, c.cust_company, p.product_name, p.spec, s.quantity, s.unitprice, s.discount, a.username, s.selldate, s.remark, s.cust_id, s.product_id, s.user_id from auth_user as a, sell as s, customer as c, product as p where s.user_id = a.id and s.cust_id = c.cust_id and s.product_id = p.product_id and s.is_alive = '1'"

    customSearch = request.GET.get('sSearch', '').rstrip().encode('utf-8');
    #if customSearch != '':
    #    rawsql = rawsql + " where address like '%" + customSearch + "%'"



    if int(request.GET.get("iSortCol_0")) == 0:
        if request.GET.get("sSortDir_0") == 'desc':
            rawsql = rawsql + " order by sell_id "
        else:
            rawsql = rawsql + " order by sell_id desc"



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
def addsale(request):
    username = request.user.username
    user_id = request.user.id
    
    if request.method == "POST":
        try:
            cust_id = request.POST.get('custid')
            product_id = request.POST.get('productid')
            quantity = request.POST.get('quantity')
            unitprice = request.POST.get('unitprice')
            discount = request.POST.get('discount')
            remark = request.POST.get('message')

            time = datetime.datetime.now()
            timenow = time.strftime("%Y-%m-%d %H:%M:%S")

            sql = "INSERT INTO sell( cust_id, product_id, user_id, quantity, unitprice, selldate, discount, remark ) VALUES('%s','%s','%s','%s', '%s', '%s', '%s', '%s')"%(cust_id, product_id, user_id, quantity, unitprice, timenow, discount, remark )
            try:
                sql_one( sql )
                success = True
                successinfo = "新增销售订单"
                return render_to_response('sale/sale.html',{
                    "title":'销售管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except:
                error = "sql error" + sql
                return render_to_response('error.html',locals())

        except:
            error = "get date error"
            return render_to_response('error.html',locals())

    return HttpResponseRedirect('/manage/sale/')




@login_required
def deletesale(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            sell_id = request.POST.get('id')
            sql = "UPDATE sell SET is_alive = '0' WHERE sell_id = '%s'"%sell_id
            try:
                sql_one( sql )
                success = True
                successinfo = "注销销售订单"
                return render_to_response('sale/sale.html',{
                    "title":'销售管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except:
                error = "sql error" + sql
                return render_to_response('error.html',locals())

        except:
            error = "get date error"
            return render_to_response('error.html',locals())
        
    return HttpResponseRedirect('/manage/sale/')



    


