import logging
import os 
from datetime import datetime

# The time format in which logging should happen
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Log path where logging is stored 
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(logs_path,exist_ok=True) # if logs directory is present then dont create 

# Logs file and logs path -> total path
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ", 
    level=logging.INFO,
)