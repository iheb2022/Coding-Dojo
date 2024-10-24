class Vehicle :
  # constructor
  def __init__(self,make_data,model_data,release_year):
    # instance attribute
    self.model = model_data
    self.year = release_year
    self.make = make_data

  # instance method to display all the attributes
  def display_info(self):
    print(f"Vehicle Info; {self.year}{self.make}{self.model}")


  

 

