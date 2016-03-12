from Ftp import *

try:
    upload_to_ftp(FtpSettings("localhost", 10022), "", "")
except Exception as e:
    print(e)