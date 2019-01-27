import configparser
import os

class ConfigHandler:
    reader = None
    def __init__(self):
        ConfigHandler.reader = configparser.ConfigParser()
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ConfigHandler.reader.read(path+"\\config\\automation_config.ini")
        return ConfigHandler.reader
    
    @staticmethod
    def getInstance():
        if ConfigHandler.reader == None:
            ConfigHandler()
        return ConfigHandler.reader
    
    