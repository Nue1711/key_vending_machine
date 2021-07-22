import datetime
import traceback
import time
from constant.path import Path
import logging

file_name = Path.PATH_FOLDER + '/logs/log-' + str(datetime.datetime.now().date()) + '.txt'
logging.basicConfig(filename=str(file_name),
                    filemode='a',
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def writeExceptionToFile():
    """ Write exception
        
        Write exception to file
    """
    logging.error(traceback.format_exc())

def writeExecutionSteps(step="", header=""):
    """ Write execution steps
        
        Write execution steps to file

        Attributes:
            step: execution step
            header: ###...###
    """
    if header == "Open":
        logging.info("#"*20 + " OPEN APP " + "#"*20)
    elif header == "Close":
        logging.info("#"*20 + " CLOSE APP " + "#"*20)
    elif header == "Start":
        logging.info("_"*17 + " START SESSION " + "_"*17)
    elif header == "Finish":
        logging.info("_"*17 + " FINISH SESSION " + "_"*17)
    else:
        if step != "":
            # write content exception
            logging.info(step)