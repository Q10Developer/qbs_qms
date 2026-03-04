# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ControlledDocument(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.document_control.doctype.document_acknowledgement.document_acknowledgement import DocumentAcknowledgement
		from frappe.document_control.doctype.iso_clause.iso_clause import ISOClause
		from frappe.types import DF

		amended_from: DF.Link | None
		approved_by: DF.Link
		change_description: DF.SmallText
		company: DF.Link
		controlled_copy: DF.Check
		department: DF.Link
		distribution_required: DF.Check
		document_acknowledgement: DF.Table[DocumentAcknowledgement]
		document_code: DF.Data
		document_content: DF.TextEditor
		document_file: DF.Attach
		document_title: DF.Data
		document_type: DF.Literal["Policy", "SOP", "WI", "Form", "Record", "Manual Template)"]
		effective_date: DF.Date
		iso_clauses: DF.Table[ISOClause]
		next_review_date: DF.Date
		prepared_by: DF.Link
		qms_process: DF.Link
		reviewed_by: DF.Link
		revision_date: DF.Date
		revision_no: DF.Data
		status: DF.Literal["Draft", "Under Review", "Approved", "Released", "Obsolete"]
	# end: auto-generated types
	pass
