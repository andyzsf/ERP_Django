;(function( $, window, document, undefined ) {

    $(document).ready(function() {
        /*change password*/
        if( $.fn.dialog  ) {
            $("#change-password-dialog").dialog({
                autoOpen: false,
                title: "修改密码",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#change-password-form').submit();
                    },
                },
            });     
        }
        
        $("#change-password").bind("click", function (event) {
            $("#change-password-dialog").dialog("open");
            event.preventDefault();
        });

        /*add class*/
        if( $.fn.dialog  ) {
            $("#add-class-dialog").dialog({
                autoOpen: false,
                title: "增加班级",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#add-class-form').submit();
                    },
                },
            });     
        }

        $("#addclass").bind("click", function (event) {
            $("#add-class-dialog").dialog("open");
            event.preventDefault();
        });

        /*select class*/
        if( $.fn.dialog  ) {
            $("#select-class-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-class-dialog").dialog("close");
                    },
                },
            });
        }

        /*edit class*/
        if( $.fn.dialog  ) {
            $("#edit-class-dialog").dialog({
                autoOpen: false,
                title: "修改班级",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#edit-class-form').submit();
                    },
                },
            });
        }
        
        /*delete class*/
        if( $.fn.dialog  ) {
            $("#delete-class-dialog").dialog({
                autoOpen: false,
                title: "删除班级",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#delete-class-form').submit();
                    },
                    "取消":function (event,ui) {
                        $("#delete-class-dialog").dialog('close');
                    },
                },
            });
        }
        
        /*add user*/
        if( $.fn.dialog  ) {
            $("#add-user-dialog").dialog({
                autoOpen: false,
                title: "增加用户",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#add-user-form').submit();
                    },
                },
            });     
        }

        if( $.fn.button  ) {
            $("#is_superuser").buttonset();
        }

        

        /*select user*/
        if( $.fn.dialog  ) {
            $("#select-user-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-user-dialog").dialog("close");
                    },
                },
            });
        }

        /*edit user*/
        if( $.fn.dialog  ) {
            $("#edit-user-dialog").dialog({
                autoOpen: false,
                title: "修改用户",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#edit-user-form').submit();
                    },
                },
            });
        }
        
        if( $.fn.button  ) {
            $("#editstudentsex").buttonset();
        }
        
        /*delete user*/
        if( $.fn.dialog  ) {
            $("#delete-user-dialog").dialog({
                autoOpen: false,
                title: "删除用户",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#delete-user-form').submit();
                    },
                    "取消":function (event,ui) {
                        $("#delete-user-dialog").dialog('close');
                    },
                },
            });
        }
        
        /*init user*/
        if( $.fn.dialog  ) {
            $("#init-user-dialog").dialog({
                autoOpen: false,
                title: "初始化密码",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#init-user-form').submit();
                    },
                    "取消":function (event,ui) {
                        $("#init-user-dialog").dialog('close');
                    },
                },
            });
        }





        /*add customer*/
        if( $.fn.dialog  ) {
            $("#add-customer-dialog").dialog({
                autoOpen: false,
                title: "增加客户",
                modal: true,
                width: "500",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#add-customer-form').submit();
                    },
                },
            });     
        }

        

        /*select customer*/
        if( $.fn.dialog  ) {
            $("#select-customer-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-customer-dialog").dialog("close");
                    },
                },
            });
        }

        /*edit customer*/
        if( $.fn.dialog  ) {
            $("#edit-customer-dialog").dialog({
                autoOpen: false,
                title: "修改客户",
                modal: true,
                width: "500",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#edit-customer-form').submit();
                    },
                },
            });
        }
        
        
        
        /*delete customer*/
        if( $.fn.dialog  ) {
            $("#delete-customer-dialog").dialog({
                autoOpen: false,
                title: "注销客户",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#delete-customer-form').submit();
                    },
                    "取消":function (event,ui) {
                        $("#delete-customer-dialog").dialog('close');
                    },
                },
            });
        }






        /*add feeder*/
        if( $.fn.dialog  ) {
            $("#add-feeder-dialog").dialog({
                autoOpen: false,
                title: "增加供应商",
                modal: true,
                width: "500",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#add-feeder-form').submit();
                    },
                },
            });     
        }

        
        /*select feeder*/
        if( $.fn.dialog  ) {
            $("#select-feeder-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-feeder-dialog").dialog("close");
                    },
                },
            });
        }

        /*edit feeder*/
        if( $.fn.dialog  ) {
            $("#edit-feeder-dialog").dialog({
                autoOpen: false,
                title: "修改供应商",
                modal: true,
                width: "500",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#edit-feeder-form').submit();
                    },
                },
            });
        }
        
        
        /*delete feeder*/
        if( $.fn.dialog  ) {
            $("#delete-feeder-dialog").dialog({
                autoOpen: false,
                title: "注销供应商",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#delete-feeder-form').submit();
                    },
                    "取消":function (event,ui) {
                        $("#delete-feeder-dialog").dialog('close');
                    },
                },
            });
        }





        /*add product*/
        if( $.fn.dialog  ) {
            $("#add-product-dialog").dialog({
                autoOpen: false,
                title: "增加产品",
                modal: true,
                width: "400",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#add-product-form').submit();
                    },
                },
            });     
        }

        
        /*select product*/
        if( $.fn.dialog  ) {
            $("#select-product-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-product-dialog").dialog("close");
                    },
                },
            });
        }

        /*edit product*/
        if( $.fn.dialog  ) {
            $("#edit-product-dialog").dialog({
                autoOpen: false,
                title: "修改产品",
                modal: true,
                width: "400",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#edit-product-form').submit();
                    },
                },
            });
        }
        
        
        /*delete product*/
        if( $.fn.dialog  ) {
            $("#delete-product-dialog").dialog({
                autoOpen: false,
                title: "注销产品",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#delete-product-form').submit();
                    },
                    "取消":function (event,ui) {
                        $("#delete-product-dialog").dialog('close');
                    },
                },
            });
        }
        





        /*add sale*/
        if( $.fn.dialog  ) {
            $("#add-sale-dialog").dialog({
                autoOpen: false,
                title: "新增销售订单",
                modal: true,
                width: "600",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#add-sale-form').submit();
                    },
                },
            });     
        }

        /*add stock*/
        if( $.fn.dialog  ) {
            $("#add-stock-dialog").dialog({
                autoOpen: false,
                title: "新增销售订单",
                modal: true,
                width: "600",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#add-stock-form').submit();
                    },
                },
            });     
        }

        
        /*select sale*/
        if( $.fn.dialog  ) {
            $("#select-sale-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-sale-dialog").dialog("close");
                    },
                },
            });
        }

        /*select stock*/
        if( $.fn.dialog  ) {
            $("#select-stock-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-stock-dialog").dialog("close");
                    },
                },
            });
        }

        /*edit sale*/
        if( $.fn.dialog  ) {
            $("#edit-sale-dialog").dialog({
                autoOpen: false,
                title: "修改产品",
                modal: true,
                width: "400",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#edit-sale-form').submit();
                    },
                },
            });
        }
        
        
        /*delete sale*/
        if( $.fn.dialog  ) {
            $("#delete-sale-dialog").dialog({
                autoOpen: false,
                title: "注销销售订单",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#delete-sale-form').submit();
                    },
                    "取消":function (event,ui) {
                        $("#delete-sale-dialog").dialog('close');
                    },
                },
            });
        }

        /*delete stock*/
        if( $.fn.dialog  ) {
            $("#delete-stock-dialog").dialog({
                autoOpen: false,
                title: "注销销售订单",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#delete-stock-form').submit();
                    },
                    "取消":function (event,ui) {
                        $("#delete-stock-dialog").dialog('close');
                    },
                },
            });
        }


        




        /*sale select customer*/
        if( $.fn.dialog  ) {
            $("#sale-select-customer-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "700",
                closeText:"hide",
                buttons: {
                    "取消": function (event,ui) {
                        $("#sale-select-customer-dialog").dialog("close");
                    },
                },
            });
        }

        /*sale select product*/
        if( $.fn.dialog  ) {
            $("#sale-select-product-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "700",
                closeText:"hide",
                buttons: {
                    "取消": function (event,ui) {
                        $("#sale-select-product-dialog").dialog("close");
                    },
                },
            });
        }


        /*stock select customer*/
        if( $.fn.dialog  ) {
            $("#stock-select-feeder-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "700",
                closeText:"hide",
                buttons: {
                    "取消": function (event,ui) {
                        $("#stock-select-feeder-dialog").dialog("close");
                    },
                },
            });
        }

        /*stock select product*/
        if( $.fn.dialog  ) {
            $("#stock-select-product-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "700",
                closeText:"hide",
                buttons: {
                    "取消": function (event,ui) {
                        $("#stock-select-product-dialog").dialog("close");
                    },
                },
            });
        }
        

        





        /*add assessment*/
        if( $.fn.dialog  ) {
            $("#add-assessment-dialog").dialog({
                autoOpen: false,
                title: "添加互评设置",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#add-assessment-form').submit();
                    },
                },
            });
        }
        
        /*delete assessment*/
        if( $.fn.dialog  ) {
            $("#delete-assessment-dialog").dialog({
                autoOpen: false,
                title: "删除互评设置",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#delete-assessment-form').submit();
                    },
                },
            });
        }
        
        /*edit assessment*/
        if( $.fn.dialog  ) {
            $("#edit-assessment-dialog").dialog({
                autoOpen: false,
                title: "修改互评设置",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#edit-assessment-form').submit();
                    },
                },
            });
        }
        
        /*select assessment*/
        if( $.fn.dialog  ) {
            $("#select-assessment-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-assessment-dialog").dialog("close");
                    },
                },
            });
        }
        
        $("#addassessment").bind("click", function (event) {
            $("#add-assessment-dialog").dialog("open");
            event.preventDefault();
        });
        
        if( $.fn.datepicker ) {
            $(".mws-datepicker").datepicker({
                showOtherMonths: true,
                dateFormat: "yy-mm-dd",
                constrainInput: true,
                minDate:"-0d",
            });
        }

        if( $.fn.datepicker ) {
            $(".mws-datepicker").datepicker({
                showOtherMonths: true,
                dateFormat: "yy-mm-dd",
                constrainInput: true,
                minDate:"-0d",
            });
        }
        
        /*num assessment*/
        if( $.fn.dialog  ) {
            $("#num-assessment-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#num-assessment-dialog").dialog("close");
                    },
                },
            });
        }
        
        /*add behavior*/
        if( $.fn.dialog  ) {
            $("#add-behavior-dialog").dialog({
                autoOpen: false,
                title: "增加日常行为活动",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#add-behavior-form").submit();
                    },
                },
            });
        }

        if( $.fn.button  ) {
            $("#addactlevel").buttonset();
        }

        $("#addbehavior").bind("click", function (event) {
            $("#add-behavior-dialog").dialog("open");
            event.preventDefault();
        });
        
        /*select behavior*/
        if( $.fn.dialog  ) {
            $("#select-behavior-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-behavior-dialog").dialog("close");
                    },
                },
            });
        }
        
        /*delete behavior*/
        if( $.fn.dialog  ) {
            $("#delete-behavior-dialog").dialog({
                autoOpen: false,
                title: "删除日常行为活动",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#delete-behavior-form").submit();
                    },
                },
            });
        }
        
        /*edit behavior*/
        if( $.fn.dialog  ) {
            $("#edit-behavior-dialog").dialog({
                autoOpen: false,
                title: "修改日常行为活动",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#edit-behavior-form").submit();
                    },
                },
            });
        }

        if( $.fn.button  ) {
            $("#editactlevel").buttonset();
        }
        
        /*add development*/
        if( $.fn.dialog  ) {
            $("#add-development-dialog").dialog({
                autoOpen: false,
                title: "增加个性发展活动",
                modal: true,
                width: "400",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#add-development-form").submit();
                    },
                },
            });
        }

        if( $.fn.button  ) {
            $("#adddevelopmentlevel").buttonset();
        }

        $("#adddevelopment").bind("click", function (event) {
            $("#add-development-dialog").dialog("open");
            event.preventDefault();
        });
        
        /*select development*/
        if( $.fn.dialog  ) {
            $("#select-development-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-development-dialog").dialog("close");
                    },
                },
            });
        }
        
        /*delete development*/
        if( $.fn.dialog  ) {
            $("#delete-development-dialog").dialog({
                autoOpen: false,
                title: "删除个性发展活动",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#delete-development-form").submit();
                    },
                },
            });
        }
        
        /*edit development*/
        if( $.fn.dialog  ) {
            $("#edit-development-dialog").dialog({
                autoOpen: false,
                title: "修改个性发展活动",
                modal: true,
                width: "400",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#edit-development-form").submit();
                    },
                },
            });
        }

        if( $.fn.button  ) {
            $("#editdevelopmentlevel").buttonset();
        }
        
        /*add comperformance_setup*/
        if( $.fn.dialog  ) {
            $("#add-comperformance_setup-dialog").dialog({
                autoOpen: false,
                title: "增加互评",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#add-comperformance_setup-form").submit();
                    },
                },
            });
        }
        
        $("#addcomperformance_setup").bind("click", function (event) {
            $("#add-comperformance_setup-dialog").dialog("open");
            event.preventDefault();
        });
        
        /*edit comperformance_setup*/
        if( $.fn.dialog  ) {
            $("#edit-comperformance_setup-dialog").dialog({
                autoOpen: false,
                title: "修改互评",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#edit-comperformance_setup-form").submit();
                    },
                },
            });
        }
        
        /*edit comperformance_setup*/
        if( $.fn.dialog  ) {
            $("#select-comperformance_setup-dialog").dialog({
                autoOpen: false,
                title: "修改互评",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-comperformance_setup-dialog").dialog("close");
                    },
                },
            });
        }
        
        /*delete comperformance_setup*/
        if( $.fn.dialog  ) {
            $("#delete-comperformance_setup-dialog").dialog({
                autoOpen: false,
                title: "删除互评",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#delete-comperformance_setup-form").submit();
                    },
                },
            });
        }

        /*select updatecomperformance*/
        if( $.fn.dialog  ) {
            $("#select-updatecomperformance-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-updatecomperformance-dialog").dialog("close");
                    },
                },
            });
        }

    });

}) (jQuery, window, document);
