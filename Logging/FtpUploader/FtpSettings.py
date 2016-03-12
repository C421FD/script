class FtpSettings:
    def __init__(self):
        self.host = "ftp://localhost:"
        self.port = "ftp://localhost:"
        self.login = "Admin"
        self.password = "11111"

    def __init__(self, host, port=21, login=None, password=None):
        self.host = host
        self.port = port
        self.login = login
        self.password = password
