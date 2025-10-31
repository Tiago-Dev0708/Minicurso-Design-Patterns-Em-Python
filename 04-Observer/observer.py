class UserEmail:
    def __init__(self, email: str, name: str):
        self.__email = email
        self.__name = name

    def notify(self, msg) -> None:
        print(f'mensagem: {msg} - Email {self.__email} - Destinatario {self.__name}')

    