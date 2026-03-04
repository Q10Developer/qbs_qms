# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ProcessInteractionMap(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		company: DF.Link
		from_process: DF.Link
		interaction_description: DF.SmallText | None
		interaction_name: DF.Data
		to_process: DF.Link
	# end: auto-generated types
	pass
