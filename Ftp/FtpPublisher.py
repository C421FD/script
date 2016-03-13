import os
from ftplib import FTP
from Log import Logger


class FtpPublisher:
    __log = Logger.get_logger(os.path.basename(__file__))
    __ftp = FTP()

    def __init__(self, server_settings):
        self.__settings__ = server_settings
        self.__ftp.encoding = 'cp1251'

    def upload_to_ftp(self, source_path, target_path):
        try:
            self.__create_connection(self.__settings__)
            self.__delete_if_exist_in_remote(os.path.basename(os.path.normpath(source_path)))
            self.__upload_directory(source_path, target_path)
            self.__ftp.quit()
        except Exception as ex:
            self.__log.error(ex)
            raise ex

    def __create_connection(self, server_settings):
        self.__log.info(str.format("Try connect to ftp server {}", server_settings.host))
        self.__ftp.connect(server_settings.host, server_settings.port)
        if server_settings.login is not None:
            self.__log.info("Authenticating on server...")
            self.__ftp.login(server_settings.login, server_settings.password)
        else:
            self.__log.info("Anonymous authentication type...")
            self.__ftp.login()

        self.__log.info("Connected to server.")

    def __upload_directory(self, local_dir, remote_dir):
        for elem in os.listdir(local_dir):
            if os.path.isfile(os.path.join(local_dir, elem)):
                self.__ftp.cwd(os.path.join(remote_dir))
                self.__delete_if_exist_in_remote(elem)
                file_to_upload = open(os.path.join(local_dir, elem), "rb")
                self.__ftp.storbinary("STOR %s" % elem, file_to_upload)
                self.__log.info(str.format("Upload file {} to {}", elem, os.path.join(elem, remote_dir)))
                file_to_upload.close()
            else:
                sub_folder = os.path.basename(os.path.normpath(elem))
                if sub_folder not in self.__ftp.nlst():
                    self.__ftp.mkd(sub_folder)
                    self.__log.info("Created folder %s" % sub_folder)

                self.__upload_directory(os.path.join(local_dir, sub_folder), os.path.join(remote_dir, sub_folder))

    def __delete_if_exist_in_remote(self, elem):
        try:
            directory_lines = self.__ftp.nlst()
            if elem in directory_lines:
                self.__log.warn("File or directory %s already exist, will be overwrite" % elem)
                try:
                    self.__ftp.delete(elem)
                except:
                    self.__ftp.rmd(elem)
        except Exception as ex:
            self.__log.error("When deleting existed file occurred exception %s" % ex)
            raise ex
