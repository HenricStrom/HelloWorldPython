from hello_world.fake_invoice_predictor import FakeInvoicePredictor
from hello_world.supplier_invoice_fetcher import get_supplier_invoices


def main():
    suppler_invoices = get_supplier_invoices()
    predictor = FakeInvoicePredictor()
    for invoice in suppler_invoices:
        is_fake = predictor.is_invoice_fake(invoice)

        print(f"Invoice {invoice.invoice_number} is {_prediction_to_string(is_fake)}.")


def _prediction_to_string(is_fake):
    return "fake" if is_fake else "real"


if __name__ == "__main__":
    main()