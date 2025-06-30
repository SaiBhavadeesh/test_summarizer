from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.model_trainer import ModelTrainer
from src.text_summarizer.logging import logger


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e
