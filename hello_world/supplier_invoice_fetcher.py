from typing import List

from hello_world.authorized_request import AuthorizedRequest
from hello_world.supplier_invoice import SupplierInvoice


def get_supplier_invoices() -> List[SupplierInvoice]:
    authorized_request = AuthorizedRequest()
    response = authorized_request.get("https://eaccountingapi-sandbox.test.vismaonline.com/v2/supplierinvoicedrafts")

    raw_supplier_invoices = response['Data']

    supplier_invoices = list()
    for raw_supplier_invoice in raw_supplier_invoices:
        supplier_invoices.append(SupplierInvoice.from_dict(raw_supplier_invoice))

    return supplier_invoices
