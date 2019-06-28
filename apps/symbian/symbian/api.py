from __future__ import unicode_literals
import frappe 

@frappe.whitelist()
def hello(phone):
    #details = frappe.get_all("Contact Info")
    return phone
