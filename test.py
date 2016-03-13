from Ftp import *

loader = FtpPublisher(FtpSettings("localhost", 10021))
loader.upload_to_ftp("C:\\source_path", "\\deploy")
