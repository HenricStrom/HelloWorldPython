import requests

from hello_world.supplier_invoice import SupplierInvoice


class FakeInvoicePredictor:
    def is_invoice_fake(self, supplier_invoice: SupplierInvoice):
        api_key = "<put your api key here>"
        url = "<put webservice url here>"
        headers = {'Authorization': f"Bearer {api_key}"}

        request_body = self._create_request_body(supplier_invoice)

        response = requests.post(url, json=request_body, headers=headers).json()

        is_fake = response['Results']['output1']['value']['Values'][0][3]
        return is_fake

    def _create_request_body(self, supplier_invoice: SupplierInvoice):
        request_body = {
            "Inputs": {
                "input1": {
                    "ColumnNames": [
                        "supplier_name",
                        "invoice_date",
                        "due_date",
                        "invoice_number",
                        "total_amount",
                        "vat",
                        "currency_code",
                        "ocr_number",
                        "message",
                        "bank_giro",
                        "is_fake"
                    ],
                    "Values": [
                        [
                            supplier_invoice.supplier_name,
                            supplier_invoice.invoice_date,
                            supplier_invoice.due_date,
                            supplier_invoice.invoice_number,
                            supplier_invoice.total_amount,
                            supplier_invoice.vat,
                            supplier_invoice.currency_code,
                            supplier_invoice.ocr_number,
                            supplier_invoice.message,
                            supplier_invoice.bank_giro_number,
                            False
                        ]
                    ]
                }
            },
            "GlobalParameters": {}
        }

        return request_body