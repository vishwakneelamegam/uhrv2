
import json
import os.path
from os import path
class fileService:
    def read_file(self,file_type):
        try:
           open_file_to_read = open(str(file_type) + ".json","r+")
           read_line_in_file = open_file_to_read.readlines()
           open_file_to_read.close()
           return read_line_in_file
        except:
           return False
    def write_file(self,file_type,data_to_write):
        try:
           open_file_to_write = open(str(file_type) + ".json","a")
           open_file_to_write.write(str(data_to_write) + "\n")
           open_file_to_write.close()
           return True
        except:
           return False
    def rewrite_file(self,file_type,data_to_write):
        try:
           open_file_to_write = open(str(file_type) + ".json","w")
           open_file_to_write.write(str(data_to_write) + "\n")
           open_file_to_write.close()
           return True
        except:
           return False

    def check_file(self,name):
        try:
           return path.exists(str(name) + ".json")
        except:
           return False
