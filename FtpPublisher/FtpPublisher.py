from ftplib import FTP
from FtpSettings import FtpSettings



def upload_to_target(server_settings):
    try:
        print(str.format("Try connect to ftp server {}", server_settings.host))
        ftp = FTP()
        ftp.connect(server_settings.host, server_settings.port)

        if server_settings.login is not None:
            print("Authenticating on server...")
            ftp.login(server_settings.login, server_settings.password)
        else:
            print("Anonymous authentication type...")
            ftp.login()

        print("Connected to server.")
        files_list = ftp.retrlines("LIST")
        print(files_list)

    except Exception as ex:
        pass


try:
    settings = FtpSettings("localhost", 10021)
    upload_to_target(settings)
except Exception as e:
    print(e)
