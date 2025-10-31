from payments import Paymentmoney, PaypalPayment
from http_request import HttpRequest


def factory_payment(tipo: str):
    if tipo == "dinheiro":
        return Paymentmoney()
    if tipo == "online":
        obj_http = HttpRequest()
        return PaypalPayment(obj_http)
    
payment = factory_payment("online")
payment.pagar(444)