import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\framework")
import ExcelHandler,LogHandler,ConfigHandler
import datetime

class Run:
    output_folder_path = None
    logger = None
    reader = None
    
    def __init__(self):
        Run.set_output_folder_path()
        Run.logger = LogHandler.LogHandler.getInstance(Run.output_folder_path+"\\logfile.log")

    
        
    @staticmethod
    def set_output_folder_path():
        Run.output_folder_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\output\\"+datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        os.mkdir(Run.output_folder_path)                            


    @staticmethod
    def execute_automation():
        Run.logger.info("This is working")

if __name__ == "__main__":
    #Instantiating All Handlers
    Run()
    Run.execute_automation()

