from logger_config import setup_logging
from schema import Patient,Report
from data import load_doctors_list
from prescription_generator import get_doctor_by_specialization,generate_prescription
from report import JsonReportGeneration,ConsoleReportGeneration


def main():
    setup_logging()
    data = load_doctors_list()
    patient_name = input("Enter patient name: ").lower()
    patient_age = int(input("Enter patient age: "))
    patient_blood_group = input("Enter patient blood group (A+,B+..): ").upper()
    patient_doctor_to_meet = input("Enter the doctor specialization to meet: ")
    
    patient = Patient(
        name=patient_name,
        age=patient_age,
        blood_group=patient_blood_group,
        doctor_specialization=patient_doctor_to_meet
    )
    doctor = get_doctor_by_specialization(patient.doctor_specialization,data)
    
    if doctor is None:
        print(f"the doctor not found for the specialization {patient.doctor_specialization}")
        return
    
    prescription = generate_prescription(doctor)

    report = Report(
        patient=patient,
        doctor=doctor,
        prescription=prescription
    )
    
    json_report = JsonReportGeneration()
    json_report.generate_report(report)
    console_report = ConsoleReportGeneration()
    console_report.generate_report(report)
    
if __name__ == "__main__":
    main()
