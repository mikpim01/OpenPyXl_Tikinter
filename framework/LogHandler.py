import logging

class LogHandler:
    logger = None
    def __init__(self,filename):
        if LogHandler.logger == None:  
            LogHandler.logger = logging.getLogger(__name__)

            # Create handlers
            f_handler = logging.FileHandler(filename)
            f_handler.setLevel(logging.INFO)

                        
            # Create formatters and add it to handlers
            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
            f_handler.setFormatter(f_format)
            
            # Add handlers to the logger
            LogHandler.logger.addHandler(f_handler)
       
    @staticmethod   
    def getInstance(filename):
        if LogHandler.logger == None:
            LogHandler(filename)
            return LogHandler.logger
        return LogHandler.logger
        