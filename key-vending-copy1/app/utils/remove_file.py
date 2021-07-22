from utils.write_log import writeExceptionToFile, writeExecutionSteps
import os
import subprocess

def removeFile(path_file):
    try:
        if os.path.isfile(path_file):
            os.remove(path_file)
            
            if not os.path.isfile(path_file):
                writeExecutionSteps("Remove file " + str(path_file) + " successful")
                return True
            else:
                return False
        else:
            return True
    except Exception:
        writeExceptionToFile()
        return False

def removeFileSubprocess(command):
    try:
        process = subprocess.Popen(command, shell=True)
    except Exception:
        writeExceptionToFile()