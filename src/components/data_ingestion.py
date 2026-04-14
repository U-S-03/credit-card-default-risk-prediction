import sys
import os
import pandas as pd
from dataclasses import dataclass
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from pathlib import Path


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(artifact_folder)
    raw_data_path: str = os.path.join(data_ingestion_dir, "card_data.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def export_data_into_raw_data_dir(self) -> pd.DataFrame:
        """
        Reads data from local dataset and saves it into artifacts
        """
        try:
            logging.info("Reading data from local dataset")

            raw_data_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(raw_data_dir, exist_ok=True)

            raw_data_path = self.data_ingestion_config.raw_data_path

            dataset = pd.read_csv("notebooks/credit_card_default_data.csv")

            logging.info(f"Saving data into: {raw_data_path}")
            dataset.to_csv(raw_data_path, index=False)

            return dataset

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> Path:
        logging.info("Entered initiate_data_ingestion method")

        try:
            self.export_data_into_raw_data_dir()

            logging.info("Data ingestion completed successfully")

            return self.data_ingestion_config.raw_data_path

        except Exception as e:
            raise CustomException(e, sys) from e
