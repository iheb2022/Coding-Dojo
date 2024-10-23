class User:
  def __init__(self,firstname,lastname,email,age):
    self.firstname=firstname
    self.lastname=lastname
    self.email=email
    self.age=age
    self.is_rewards_member=False
    self.gold_card_point=0
  
  def display_info(self):
    print(self.firstname)
    print(self.lastname)
    print(self.email)
    print(self.age)
    print(self.is_rewards_member)
    print(self.gold_card_point)

  
  def enroll(self):
    self.is_rewards_member=True
    self.gold_card_point=200

  def spend_points(self,amount):
    self.gold_card_point=self.gold_card_point -(amount)



peter= User ("Peter","Parker","peterparker@gmail.com",30)
peter.display_info().enroll().spend_points(50).display_info()

David= User ("David","Beckham","DavidBeckam@gmail.com",48)
David.display_info().enroll().spend_points(80).display_info()







