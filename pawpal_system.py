from dataclasses import dataclass, field
from typing import List


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    weight: float
    medical_history: List[str] = field(default_factory=list)

    def get_profile(self) -> str:
        pass

    def add_medical_record(self, record: str) -> None:
        pass

    def update_weight(self, weight: float) -> None:
        pass


@dataclass
class Appointment:
    date: str
    type: str
    pet: Pet
    provider: "Caregiver"
    notes: str = ""

    def reschedule(self, new_date: str) -> None:
        pass

    def cancel(self) -> None:
        pass

    def get_summary(self) -> str:
        pass


class Owner:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def get_contact_info(self) -> str:
        pass


class Caregiver:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.availability: List[str] = []
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, appointment: Appointment) -> None:
        pass

    def get_upcoming_appointments(self) -> List[Appointment]:
        pass

    def is_available(self, date: str) -> bool:
        pass
