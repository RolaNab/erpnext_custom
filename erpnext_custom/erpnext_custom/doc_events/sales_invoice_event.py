import frappe

@frappe.whitelist()
def validate_add_custome_remarks(doc,method):
    items = ""
    for item in doc.get("items"):
        items = str(items) + " \n " + str(item.item_code)
    doc.remarks = str(items)

@frappe.whitelist()
def validate_note_remarks(doc,method):
    notes = ""
    notes = str(notes) + " \n " + str(doc.note)
    doc.remarks = str(notes)

@frappe.whitelist()
def check_pos_payment(doc,method):
    if doc.is_pos:
        payments = 0
        for item in doc.get("payments"):
            payments = float(item.amount)
        if payments == 0:
            frappe.throw("Payment amount must be more than 0")
