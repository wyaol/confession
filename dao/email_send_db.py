from .db_tool import SQL


class EmailSend:

    def __init__(self):
        self.table_name = 'teenagers'
        self.sql_client = SQL()

    def add_email_sender(self, email, name, sex, o_email, o_name):
        self.sql_client.insert(self.table_name, email=email, name=name, o_email=o_email, o_name=o_name, sex=sex)

    def update_email_sender(self, email, name, sex, o_email, o_name):
        self.sql_client.update(
            self.table_name,
            {
                'email': email,
                'name': name,
                'o_email': o_email,
                'o_name': o_name,
                'sex': sex
            },
            {
                'email': email
            }
        )

    def if_sender_exist(self, email):
        res = self.sql_client.select(self.table_name, ['*'], email=email)
        if len(res) > 0: return True
        return False

    def add_email(self, email: str, o_email: str, cont: str, state: int):
        self.sql_client.insert('emails', email=email, o_email=o_email, cont=cont, state=state)