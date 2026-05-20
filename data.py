import json
import logging
from schema import Doctor
from pydantic import TypeAdapter
from pathlib import Path

DATA_FILE = Path(__file__).parent / "doctors.json"

logger = logging.getLogger(__name__)

def load_doctors_list():
  '''This fuction loads the doctors json file and validates the types'''
  logger.info("Loading doctors list...")
  try:
    with open(DATA_FILE) as file:
      raw_doctores_list = json.load(file)
  except FileNotFoundError:
    logger.exception("The Doctors.json file not found")
    return []
  adapter = TypeAdapter(list[Doctor])
  doctors_list = adapter.validate_python(raw_doctores_list)
  logger.info(f"Loaded {len(doctors_list)} doctors successfully")
  return doctors_list
  