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

# Hospital Class
class Hospital:

    def __init__(self, hospital_name):
        self.hospital_name = hospital_name

    def display(self):
        print("Hospital:", self.hospital_name)


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
