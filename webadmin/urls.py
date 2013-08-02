#!/usr/bin/python
#-*-coding:utf-8-*-

from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webadmin.views.home', name='home'),
    # url(r'^webadmin/', include('webadmin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^grappelli/',include('grappelli.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    #favicon.ico
    url(r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.png'}),

    url(r'^accounts/login/$', 'engine.account.userlogin',name="userlogin"),
    url(r'^accounts/logout/$',  'django.contrib.auth.views.logout',
                                {'next_page': '/accounts/login/'},name="userlogout"),
    url(r'^accounts/changepassword/$', 'engine.account.changepassword',name="changepassword"),
    url(r'^$', 'engine.views.index'),

  



    #feeder
    url(r'^manage/feeder/$', 'engine.feeder.index',name="managefeeder"),
    url(r'^manage/addfeeder/$', 'engine.feeder.addfeeder',name="addfeeder"),
    url(r'^manage/editfeeder/$', 'engine.feeder.editfeeder',name="editfeeder"),
    url(r'^manage/deletefeeder/$', 'engine.feeder.deletefeeder',name="deletefeeder"),
    #feeder ajax
    url(r'^ajax/get_feeders_list/$', 'engine.feeder.get_feeders_list',name="get_feeders_list"),


    

    #customer
    url(r'^manage/customer/$', 'engine.customer.index',name="managecustomer"),
    url(r'^manage/addcustomer/$', 'engine.customer.addcustomer',name="addcustomer"),
    url(r'^manage/editcustomer/$', 'engine.customer.editcustomer',name="editcustomer"),
    url(r'^manage/deletecustomer/$', 'engine.customer.deletecustomer',name="deletecustomer"),
    #customer ajax
    url(r'^ajax/get_customers_list/$', 'engine.customer.get_customers_list',name="get_customers_list"),


    #product
    url(r'^manage/product/$', 'engine.product.index',name="manageproduct"),
    url(r'^manage/addproduct/$', 'engine.product.addproduct',name="addproduct"),
    url(r'^manage/editproduct/$', 'engine.product.editproduct',name="editproduct"),
    url(r'^manage/deleteproduct/$', 'engine.product.deleteproduct',name="deleteproduct"),
    #product ajax
    url(r'^ajax/get_products_list/$', 'engine.product.get_products_list',name="get_products_list"),


    #sale
    url(r'^manage/sale/$', 'engine.sale.index',name="managesale"),
    url(r'^manage/addsale/$', 'engine.sale.addsale',name="addsale"),
    url(r'^manage/deletesale/$', 'engine.sale.deletesale',name="deletesale"),
    #sale ajax
    url(r'^ajax/get_sales_list/$', 'engine.sale.get_sales_list',name="get_sales_list"),


    #hub
    url(r'^manage/hub/$', 'engine.hub.index',name="managehub"),
    #hub ajax
    url(r'^ajax/get_hubs_list/$', 'engine.hub.get_hubs_list',name="get_hubs_list"),


    #hubalarm
    url(r'^manage/hubalarm/$', 'engine.hub.hubalarm',name="managehubalarm"),
    #hubalarm ajax
    url(r'^ajax/get_hubalarm_list/$', 'engine.hub.get_hubalarm_list',name="get_hubalarm_list"),
    

    #profit
    url(r'^manage/profit/$', 'engine.profit.index',name="manageprofit"),
    #profit ajax
    url(r'^ajax/get_profit_list/$', 'engine.profit.get_profit_list',name="get_profit_list"),




    #stock
    url(r'^manage/stock/$', 'engine.stock.index',name="managestock"),
    url(r'^manage/addstock/$', 'engine.stock.addstock',name="addstock"),
    url(r'^manage/deletestock/$', 'engine.stock.deletestock',name="deletestock"),
    #stock ajax
    url(r'^ajax/get_stocks_list/$', 'engine.stock.get_stocks_list',name="get_stocks_list"),

    
    #user
    url(r'^manage/user/$', 'engine.user.index',name="manageuser"),
    url(r'^manage/adduser/$', 'engine.user.adduser',name="adduser"),
    url(r'^manage/edituser/$', 'engine.user.edituser',name="edituser"),
    url(r'^manage/deleteuser/$', 'engine.user.deleteuser',name="deleteuser"),
    url(r'^manage/inituser/$', 'engine.user.inituser',name="inituser"),
    #url(r'^studentprofile/$', 'engine.user.userprofile',name="studentprofile"),
    #user ajax
    url(r'^ajax/get_users_list/$', 'engine.user.get_users_list',name="get_users_list"),
    #url(r'^ajax/select_classes/$', 'engine.class.select_classes',name="select_classes"),







    
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve',{'document_root':settings.STATIC_ROOT}),
    )
