from logger_config import setup_logger
from exception import CustomException
import sys

logger = setup_logger()

logger.info("This is a test log message.")

try:
    a = 1 / 0
except Exception as e:
    logger.info("Logging the exception")
    raise CustomException(e, sys)
