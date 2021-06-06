#Learning about object orientated python

class Participant():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score # 1-1000

    def Score(self):
        return self.score

class Swimming_Learning:
    def __init__(self,name,max):
        self.name = name
        self.max = max
        self.participant = []

    def Passing_Courses(self,participant):
        if len(self.participant) < self.max:
            self.participant.append(participant)
            return True
        return False

    def get_study(self):
        value = 0
        for participant in self.participant:
            value += participant.get.score(self)
        
        return value / len(self.participant)


p_1 = Participant("vito", 19, 800)
p_2 = Participant("Willy", 17, 850)
p_3 = Participant("Gabriel", 19, 600)

learning = Swimming_Learning("Passing Learning", 2)
learning.Passing_Courses(p_1)
learning.Passing_Courses(p_2)
learning.Passing_Courses(p_3)
print(Swimming_Learning.get_study(learning))