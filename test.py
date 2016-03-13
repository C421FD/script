from Ftp import *

loader = FtpPublisher(FtpSettings("localhost", 10022))
loader.upload_to_ftp("C:\\source_path", "\\deploy")
