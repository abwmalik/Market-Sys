from erpnext.erpnext.stock.doctype.batch.batch import Batch

class CustomBatch(Batch):
    def validate(self):
		self.item_has_batch_enabled()
		self.set_batchwise_valuation()


# Add this function
def set_batch_nos(doc, warehouse_field, throw=False):
    """Automatically select `batch_no` for outgoing items in item table"""
    for d in doc.items:
        qty = d.get('stock_qty') or d.get('transfer_qty') or d.get('qty') or 0
        has_batch_no = frappe.db.get_value('Item', d.item_code, 'has_batch_no')
        warehouse = d.get(warehouse_field, None)
        if has_batch_no and warehouse and qty > 0:
            if not d.batch_no:
                d.batch_no = get_batch_no(d.item_code, warehouse, qty, throw, d.serial_no)
            else:
                batch_qty = get_batch_qty(batch_no=d.batch_no, warehouse=warehouse)
                if flt(batch_qty, d.precision("qty")) < flt(qty, d.precision("qty")):
                frappe.throw(_("Row #{0}: The batch {1} has only {2} qty. Please select another batch which has {3} qty available or split the row into multiple rows, to deliver/issue from multiple batches").format(d.idx, d.batch_no, batch_qty, qty))
                