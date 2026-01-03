from exception import CustomException
from logger_config import setup_logger
import sys

logger = setup_logger()

try:
    a = 1 / 0
except Exception as e:
    logger.info("Division by zero error")
    raise CustomException(e, sys)
