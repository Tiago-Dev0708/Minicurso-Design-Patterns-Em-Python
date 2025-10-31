from abc import ABC, abstractmethod

class PaymentServiceInterface(ABC): #Não Pode Instanciar Um Objeto

    @abstractmethod
    def pagar(self, valor: float):
        pass

class PaypalPayment(PaymentServiceInterface):
    def pagar(self, valor: float):
        pass

class Paymentmoney(PaymentServiceInterface):
    def pagar(self, valor: float):
        pass