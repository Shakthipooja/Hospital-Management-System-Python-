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
    
