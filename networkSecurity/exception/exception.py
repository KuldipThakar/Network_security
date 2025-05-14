import sys
from  networkSecurity.logging import logger

class NetworkSecutityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        # Extracting the line number and file name from the exception traceback
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in python script name [{self.file_name}] line number [{self.lineno}] error message [{self.error_message}]"

    
'''if __name__ == '__main__':
    try:
        logger.info("Enter the try block")
        a = 1/0
        print("this should not be printed due to error is generated above")
    except Exception as e:
        raise NetworkSecutityException(e,sys)
        
        this is just for the test '''
    