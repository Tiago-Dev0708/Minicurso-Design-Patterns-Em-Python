from observer import UserEmail
from subject import EmailHandler

observer1 = UserEmail("clodoaldo@gmail.com", "Clodoaldo")
observer2 = UserEmail("cleiton@gmail.com", "Cleiton")
observer3 = UserEmail("josivaldo@gmail.com", "Josivaldo")

email_handler = EmailHandler()

email_handler.add_observer(observer1)
email_handler.add_observer(observer2)
email_handler.add_observer(observer3)

msg = "O pagamento foi confirmado"

email_handler.send_email(msg)