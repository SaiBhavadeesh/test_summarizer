from src.text_summarizer.logging import logger
from src.text_summarizer.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from src.text_summarizer.pipeline.stage_2_data_transformation import (
    DataTransformationPipeline,
)

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    raise e
