import frappe
from frappe.utils import time_diff_in_hours


def validate_attendence(doc,method):
    get_hours = time_diff_in_hours(doc.check_out,doc.check_in)
    doc.hours = get_hours
    if not doc.check_in or doc.check_out:
        doc.status = 'Absent'
