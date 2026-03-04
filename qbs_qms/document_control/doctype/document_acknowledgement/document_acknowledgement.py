# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DocumentAcknowledgement(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		acknowledged: DF.Check
		acknowledgement_on: DF.Datetime | None
		department: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		user: DF.Link
	# end: auto-generated types
	pass
