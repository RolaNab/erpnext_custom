import frappe


def validate(doc, method):
    validate_add_custome_remarks(doc)
    validate_note_remarks(doc)
    check_pos_payment(doc)
    # allow_discount(customer_id)
    # check_discounts(doc)


@frappe.whitelist()
def validate_add_custome_remarks(doc, method):
    items = ""
    for item in doc.get("items"):
        items = str(items) + " \n " + str(item.item_code)
    doc.remarks = str(items)


@frappe.whitelist()
def validate_note_remarks(doc, method):
    notes = ""
    notes = str(notes) + " \n " + str(doc.note)
    doc.remarks = str(notes)


@frappe.whitelist()
def check_pos_payment(doc, method):
    if doc.is_pos:
        payments = 0
        for item in doc.get("payments"):
            payments = float(item.amount)
        if payments == 0:
            frappe.throw("Payment amount must be more than 0")


# @frappe.whitelist(allow_guest=True)
# def allow_discount(customer_id):
#     allow_disc = frappe.get_value("Customer", customer_id, "allow_discount")
#     if allow_disc == 0:
#         return True
#     return False

# @frappe.whitelist(allow_guest=True)
# def check_discounts(doc):
#     allow_discount = frappe.get_value("Customer", doc.customer, "allow_discount")
#     if allow_discount == 1:
#         return True
#     return False
