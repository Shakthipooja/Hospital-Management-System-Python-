#Hospital Class
class HospitaL:
  def __init__(self, hospital_name):
    self.hosital_name = hospital_name
  def display(self):
    print("Hospital: ",self.hospital_name)

#Create object
hospital = Hospital("Apollo Hospital")
#Display
hospital.display()
# Patient Class
class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
    def display(self):
        print("\nPatient Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
# Create objects
hospital = Hospital("Apollo Hospital")
patient = Patient(
    "Arun",
    45,
    "Diabetes"
)

# Display details
hospital.display()
patient.display()
# Doctor Class
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
    def display(self):
        print("\nDoctor Details")
        print("Name:", self.name)
        print("Specialization:", self.specialization)
# Create objects
hospital = Hospital("Apollo Hospital")
patient = Patient(
    "Arun",
    45,
    "Diabetes"
)
doctor = Doctor(
    "Dr. Kumar",
    "Cardiology"
)
# Display
hospital.display()
patient.display()
doctor.display()
hospital.display()
patient.display()
