# train.py

import dagshub
import mlflow
from logger_config import setup_logger

# Setup logger
logger = setup_logger()

logger.info("Starting training script")

dagshub.init(
    repo_owner="anushkamali-2005",
    repo_name="agrix",
    mlflow=True
)

mlflow.set_experiment("agrix-test")

with mlflow.start_run():
    logger.info("MLflow run started")

    mlflow.log_param("epochs", 10)
    mlflow.log_metric("accuracy", 0.94)

    logger.info("Metrics logged successfully")

logger.info("Training completed")
