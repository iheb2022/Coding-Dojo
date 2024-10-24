



# child
# inheritance (one of the 4 pillars)
from Vehicle import Vehicle


class Car(Vehicle):
  def __init__(self, make_data, model_data, release_year, number_of_doors):
    super().__init__(make_data, model_data, release_year)
    self.number_of_doors = number_of_doors
  # polymorphism
  def display_info(self):
    super().display_info()
    print(f"number of doors : {self.number_of_doors}")