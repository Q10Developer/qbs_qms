# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ISOClause(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		clause_code: DF.Data
		clause_level: DF.Literal["4 Context of Organization", "5 Leadership", "6 Planning", "7 Support", "8 Operation", "9 Performance Evaluation", "10 Improvement"]
		clause_title: DF.Data
		description: DF.TextEditor | None
	# end: auto-generated types
	pass
