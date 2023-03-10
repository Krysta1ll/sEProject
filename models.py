class User:
    '所有用户的基类'
    empCount = 0

    def __init__(self, username, password, email):
        self.userName = username
        self.password = password
        self.email = email
