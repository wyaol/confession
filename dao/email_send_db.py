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

    def if_exist_sender(self, email):
        return self.if_exist(self.table_name, email=email)

    def add_email(self, email: str, o_email: str, cont: str, state: int):
        self.sql_client.insert('emails', email=email, o_email=o_email, cont=cont, state=state)

    def if_exist_code(self, email):
        return self.if_exist('code', email=email)

    def if_exist(self, table_name, **kwargs) -> bool:
        """
        查找某记录是否存在
        :param table_name: 表名
        :param kwargs: 限定条件
        :return: true false
        """
        res = self.sql_client.select(table_name, ['*'], **kwargs)
        if len(res) > 0: return True
        return False

    def add_code(self, email, code):
        self.sql_client.insert('code', email=email, code=code)

    def del_code(self, email):
        self.sql_client.delete('code', email=email)

    def get_code(self, email):
        """
        从数据库中查找验证码
        :param email: key值
        :return:
        """
        res = self.sql_client.select('code', ['code'], email=email)
        if len(res) == 0: return ''
        return res[0][0]

    def if_exist_pair(self, email, o_email):
        return self.if_exist('emails', email=o_email, o_email=email)
    
    def get_current_send_timestamp(self, email):
        self.sql_client.cursor.execute("select send_time from emails where email = '%s' order by send_time desc" % (email))
        res = self.sql_client.cursor.fetchall()
        if len(res) == 0: return 0
        return res[0][0]