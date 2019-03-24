# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "accounts_export"
app_title = "Accounts Export"
app_publisher = "ALYF.de ERPNext Consulting"
app_description = "Export Accounts data in a CSV Dialect of your choice"
app_icon = "octicon octicon-repo-pull"
app_color = "green"
app_email = "hallo@alyf.de"
app_license = "GPLv3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/accounts_export/css/accounts_export.css"
# app_include_js = "/assets/accounts_export/js/accounts_export.js"

# include js, css files in header of web template
# web_include_css = "/assets/accounts_export/css/accounts_export.css"
# web_include_js = "/assets/accounts_export/js/accounts_export.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "accounts_export.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "accounts_export.install.before_install"
# after_install = "accounts_export.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "accounts_export.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"accounts_export.tasks.all"
# 	],
# 	"daily": [
# 		"accounts_export.tasks.daily"
# 	],
# 	"hourly": [
# 		"accounts_export.tasks.hourly"
# 	],
# 	"weekly": [
# 		"accounts_export.tasks.weekly"
# 	]
# 	"monthly": [
# 		"accounts_export.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "accounts_export.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "accounts_export.event.get_events"
# }

