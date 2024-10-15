import csv
from typing import Dict


def load_csv(file_path: str) -> list[Dict]:
    """
    Load a CSV file in memory and return a list of dictionaries
    file_path: str: Path to the CSV file
    return: list[Dict]: List of dictionaries row mapping column names to values
    """
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
    return list(reader)

