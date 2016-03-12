import os
from ftplib import FTP

from Log import Logger

log = Logger.get_logger(os.path.basename(__file__))


def upload_to_ftp(server_settings, source_path, target_path):
    try:
        create_connection(server_settings)
        pass
        pass
    except Exception as ex:
        log.error(ex)


def create_connection(server_settings):
    log.info(str.format("Try connect to ftp server {}", server_settings.host))
    ftp = FTP()
    ftp.connect(server_settings.host, server_settings.port)
    if server_settings.login is not None:
        log.info("Authenticating on server...")
        ftp.login(server_settings.login, server_settings.password)
    else:
        log.info("Anonymous authentication type...")
        ftp.login()
    log.info("Connected to server.")
    files_list = ftp.retrlines("LIST")
    log.info(files_list)
