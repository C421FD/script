class FtpSettings:
    @staticmethod
    def default():
        return FtpSettings("localhost")

    def __init__(self, host, port=21, login=None, password=None):
        self.host = host
        self.port = port
        self.login = login
        self.password = password
