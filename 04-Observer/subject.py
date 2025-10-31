class EmailHandler:
    def __init__(self):
        self.__emails = []

    def send_email(self, msg) -> None:
        if msg == "":
            return
        else:
            for email in self.__emails:
                email.notify(msg)

    def add_observer(self, email) -> None:
        self.__emails.append(email)