frappe.ui.form.on('Sales Invoice', {
	customer: function(frm) {
	    frappe.call({
            method: 'erpnext_custom.erpnext_custom.doc_events.sales_invoice_event.allow_discount',
            args: {
                'customer_id': frm.doc.customer_id
            },
            callback: function(r) {
                if (r.message) {
                alert(r.message)
                console.log(r.message)
//                    frm.set_df_property('apply_discount_on', 'disabled', 1)
//
//                    frm.set_df_property('is_cash_or_non_trade_discount', 'disabled')
//
//                     frm.set_value('additional_discount_account', 0);
//                    frm.set_df_property('additional_discount_account','disabled', 1)
//
//                    frm.set_value('additional_discount_percentage', 0);
//                    frm.set_df_property('additional_discount_percentage','disabled', 1)
//
//                    frm.set_value('discount_amount', 0);
//                    frm.set_df_property('discount_amount','disabled', 1)
                }
//                else if (r.message == false){
//                   frm.set_df_property('apply_discount_on', 'disabled', 0)
//
//                    frm.set_df_property('is_cash_or_non_trade_discount', 'disabled' , 0)
//
//                    frm.set_value('additional_discount_account', 0);
//                    frm.set_df_property('additional_discount_account','disabled', 0)
//
//                    frm.set_value('additional_discount_percentage', 0);
//                    frm.set_df_property('additional_discount_percentage','disabled', 0)
//                  }
            }
        });
	}


});



// args: {
//                'doctype': 'Customer',
//                'fieldname': ['frm.doc.allow_discount']
//            },

