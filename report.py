import json
import logging
from schema import Report
from interface import IReportGenerator
from pathlib import Path

logger = logging.getLogger(__name__)

class JsonReportGeneration(IReportGenerator):
  def generate_report(self, report:Report):
    report_dict = report.model_dump(exclude={"doctor": {"medicines"}})
    Path("reports").mkdir(exist_ok=True)
    filename = f'{report.report_id}.json'
    with open(Path("reports")/filename,"w") as file:
      json.dump(report_dict,file,indent=4,default=str)
    logger.info(f"Report saved: {filename}")
    
class ConsoleReportGeneration(IReportGenerator):
  def generate_report(self, report:Report):
    print("==================================")
    print(f"Patientname is: {report.patient.name}")
    print(f"age is: {report.patient.age}")
    print(f"blood group is: {report.patient.blood_group}")
    print(f"doctor specialization is: {report.patient.doctor_specialization}")
    print(f"doctor met: {report.doctor.name}")
    print(f"Prescription: {report.prescription}")
    print("===================================")