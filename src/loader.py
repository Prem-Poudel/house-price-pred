"""
This file will be used to load the data, pipeline and transformers
"""

import pandas as pd
import joblib

from src.config import DATASET_PATH, PIPELINE_PATH, MEDIAN_ADDER_PATH



def unique_values_load():
    """
    This function will be used to load the unique values present in the city and locality columns.
    """
    
    try:
        df = pd.read_csv(DATASET_PATH)
        unique_cities = sorted(df['city'].unique())
        unique_localities = sorted(df['locality'].unique())
        unique_property_types = sorted(df['property_type'].unique())
        unique_furnished = sorted(df['furnished'].unique())

        return unique_cities, unique_localities, unique_property_types, unique_furnished
    
    except Exception as e:
        raise Exception(f"Error loading unique values: {e}")


def pipeline_load():
    """
    This function will be used to load the pipeline and transformers
    """
    try:
        pipeline = joblib.load(PIPELINE_PATH)
        median_adder = joblib.load(MEDIAN_ADDER_PATH)
        return pipeline, median_adder
    
    except Exception as e:
        raise Exception(f"Error loading pipeline: {e}")
