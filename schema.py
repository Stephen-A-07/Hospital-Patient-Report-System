from pydantic import BaseModel,Field
from uuid import uuid4
from blood_group_enum import BloodGroup
from datetime import datetime


class Patient(BaseModel):
    patient_id: str = Field(default_factory=lambda: str(uuid4()),description="Auto generated patient id")
    name: str = Field(min_length=3,max_length=100,description="Patient name")
    age: int = Field(ge=1,le=100,description="Patient age")
    blood_group: BloodGroup
    doctor_specialization: str = Field(
        min_length=3, description="Medical specialization"
    )


class Doctor(BaseModel):
    doctor_id: str = Field(
        ...,pattern=r"^DOC-\d{3}$", description="Unique doctor_id with pattern DOC-001"
    )
    name: str = Field(
        ..., min_length=3, max_length=100, description="Doctor name"
    )
    specialization: str = Field(
        ..., min_length=3, max_length=30, description="Doctors specialization"
    )
    medicines: list[str] = Field(
        ..., min_length=3, max_length=20, description="List of medicines"
    )


class Report(BaseModel):
    report_id: str = Field(default_factory=lambda: str(uuid4()))
    patient: Patient
    doctor:Doctor
    visit_time: datetime = Field(default_factory=datetime.now)
    prescription: list[str]
