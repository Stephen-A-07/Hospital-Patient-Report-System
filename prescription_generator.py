import logging
from schema import Doctor
import random

logger = logging.getLogger(__name__)


def get_doctor_by_specialization(specialization:str,doctors:list[Doctor])->Doctor|None :
  matched_doctors = [doc for doc in doctors if doc.specialization == specialization]
  if not matched_doctors:
    logger.warning("There is no matching doctors please inform the patient to visit another day")
    return None
  randomly_selected_doctor = random.choice(matched_doctors)
  return randomly_selected_doctor
  
def generate_prescription(doctor:Doctor)->list[str]:
  random_prescription = list(random.sample(doctor.medicines,4))
  logger.info(f"Selected doctor:{doctor} and prescription: {random_prescription}")
  return random_prescription
    