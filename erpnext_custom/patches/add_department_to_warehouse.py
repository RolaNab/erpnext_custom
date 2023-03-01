import frappe

def execute():
    frappe.db.sql(""" update `tabWarehouse` set department= 'Accounts'  """)