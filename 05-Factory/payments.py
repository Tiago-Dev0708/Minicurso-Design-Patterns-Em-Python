from payment_interface import PaymentServiceInterface


class PaypalPayment(PaymentServiceInterface):
    def __init__(self, http):
        self.http_request = http

    def pagar(self, valor: float):
        self.http_request.post(valor)
        print("Pagamento realizado")

class Paymentmoney(PaymentServiceInterface):
    def pagar(self, valor: float):
        pass