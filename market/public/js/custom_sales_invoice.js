// Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sales Invoice", {
    // onload: function (frm) {
    //     if (frm.is_new() && !frm.doc.due_date) {
    //         // Get today's date
    //         const today = frappe.datetime.now_date(); // Returns YYYY-MM-DD
    //         // Format the date to DD-MM-YYYY
    //         const formatted_date = frappe.datetime.str_to_user(today); 
    //         // Set the due_date field
    //         frm.set_value('due_date', formatted_date);
    //     }
    // }
    refresh: function (frm) {
        // Hide the 'Customer' field
        frm.set_df_property('customer', 'hidden',1);
    }

});
