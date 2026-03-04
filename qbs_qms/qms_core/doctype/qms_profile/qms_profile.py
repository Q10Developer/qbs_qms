# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class QMSProfile(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.qms_core.doctype.qms_site.qms_site import QMSSite
		from frappe.types import DF

		applicable_standards: DF.SmallText | None
		cert_expiry_date: DF.Date | None
		cert_issue_date: DF.Date | None
		certificate_no: DF.Data | None
		certification_body: DF.Data | None
		company: DF.Link | None
		exclusions: DF.SmallText | None
		management_rep: DF.Link
		qms_scope: DF.SmallText
		qms_site: DF.Table[QMSSite]
	# end: auto-generated types
	pass
