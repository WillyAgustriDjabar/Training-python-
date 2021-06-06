#Learning Object oriantated python

class Participants():
    def __init__(self,name,years):
        self.name = name
        self.years = years

    def participant(self):
        print("\nNama :", self.name,"\nUmur :", self.years)

   
        
        
print("\n", "participant : ")

p_1 = Participants("Vito",19)
p_1.participant()

p_2 = Participants("Ipan", 19)
p_2.participant()

p_3 = Participants("Willy", 17)
p_3.participant()

class SwimmingPool(Participants):
    def __init__(self,name,years,result, rank):
      super().__init__(name,years)
      self.result = result
      self.rank = rank



    def swimming(self):
         print("\nNama :", self.name,"\nUmur :", self.years, self.result)


    def rank(self):
        if len(self.result) < self.rank:
            print("congratulation")

print("\n", "result for participant of Swimming is :")

p_1 = SwimmingPool("Vito",19, 60,1)
p_1.swimming()

p_2 = SwimmingPool("Ipan", 19, 75,2)
p_2.swimming()

p_3 = SwimmingPool("Willy", 17,75,3)
p_3.swimming()
p_3.rank()

