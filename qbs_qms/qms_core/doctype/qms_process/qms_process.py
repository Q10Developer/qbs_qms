# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class QMSProcess(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.qms_core.doctype.process_iso_clause.process_iso_clause import ProcessISOClause
		from frappe.qms_core.doctype.process_kpi.process_kpi import ProcessKPI
		from frappe.qms_core.doctype.process_link.process_link import ProcessLink
		from frappe.types import DF

		company: DF.Link
		department: DF.Link
		downstream_processes: DF.Table[ProcessLink]
		inputs: DF.SmallText | None
		iso_clauses: DF.Table[ProcessISOClause]
		kpis: DF.Table[ProcessKPI]
		outputs: DF.SmallText | None
		process_code: DF.Data | None
		process_link: DF.Table[ProcessLink]
		process_name: DF.Data
		process_owner: DF.Link
		purpose: DF.SmallText | None
		upstream_processes: DF.Table[ProcessLink]
	# end: auto-generated types
	pass
