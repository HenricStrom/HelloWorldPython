class SupplierInvoice:
    def __init__(self):
        self.id = ""
        self.supplier_id = ""
        self.bank_account_id = ""
        self.invoice_date = ""
        self.payment_date = ""
        self.due_date = ""
        self.invoice_number = ""
        self.total_amount = 0
        self.vat = 0
        self.vat_high = 0
        self.vat_medium = 0
        self.vat_low = 0
        self.is_credit_invoice = False
        self.currency_code = ""
        self.currency_rate = 0
        self.ocr_number = ""
        self.message = ""
        self.plus_giro_number = ""
        self.bank_giro_number = ""
        self.rows = list()
        self.supplier_name = ""
        self.supplier_number = ""
        self.remaining_amount = 0
        self.remaining_amount_invoice_currency = 0
        self.voucher_number = ""
        self.voucher_id = ""
        self.created_from_draft_id = ""
        self.self_employed_without_fixed_address = False
        self.allocation_periods = list()
        self.attachments = list()

    @classmethod
    def from_dict(cls, raw_supplier_invoice):
        supplier_invoice = cls()

        for attribute_name in supplier_invoice.__dict__.keys():
            attribute_name_as_cc = _to_camel_case(attribute_name)
            setattr(supplier_invoice, attribute_name, raw_supplier_invoice.get(attribute_name_as_cc))

        return supplier_invoice


def _to_camel_case(snake_case: str):
    words = snake_case.split("_")
    return "".join(map(str.capitalize, words))