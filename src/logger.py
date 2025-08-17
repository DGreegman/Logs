import logging, sys, os
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv
from logtail import LogtailHandler



load_dotenv()

token = os.getenv('TOKEN')

# get the root logger 

logger = logging.getLogger(__name__)

# create a formatter

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# create handlers
file_handler = TimedRotatingFileHandler('logs.log', when='D', interval=1, backupCount=7)
stream_handler = logging.StreamHandler(sys.stdout)
better_stack_handler = LogtailHandler(source_token=token)




# set the formatter 
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


# add the handlers to the logger

logger.handlers = [file_handler, stream_handler, better_stack_handler]

# set log level
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)

