




from Vehicle import Vehicle


class Motorcycle(Vehicle):
  def __init__(self, make_data, model_data, release_year,type_of_handlebars):
    super().__init__(make_data, model_data, release_year)
    self.type_of_handlebars=type_of_handlebars

  def display_info(self):
    super().display_info()
    print(f"Type of Handlebars:{self.type_of_handlebars}")

