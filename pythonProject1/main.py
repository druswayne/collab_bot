from random import random, randint,shuffle

list_ = [{"text": "2+2",
         "diff": 1,
         "RightAnswer": 4},

         {"text": "6+4",
         "diff": 1,
         "RightAnswer": 10},

        {"text": "10+22",
         "diff": 2,
         "RightAnswer": 32},

         {"text": "16+12",
         "diff": 2,
         "RightAnswer": 28},

         {"text": "4*6",
         "diff": 3,
         "RightAnswer": 24},

         {"text": "7*8",
         "diff": 3,
         "RightAnswer": 56},

         {"text": "(13+10)*6",
         "diff": 4,
         "RightAnswer": 138},

         {"text": "(15*4)/6",
         "diff": 4,
         "RightAnswer": 10},

         {"text": "((√81 * 11) + (21 / 7) - 100) * 5!",
         "diff": 5,
         "RightAnswer": 240},

         {"text": "(1467*43+2334/2-132*2+900/455+654389-15*10-59+15037)*0+2*6,5",
         "diff": 5,
         "RightAnswer": 13}
        ]
score = 0
class Question:

     def __init__(self, text, diff, RightAnswer):
        self.text = text
        self.diff = diff
        self.RightAnswer = RightAnswer
        #self.que = que
        self.que = False
        #self.answer = answer
        self.answer = None
        self.points = self.get_points()

     def get_points(self):
         return(self.diff * 10)

     def is_correct(self):
         if self.answer == self.RightAnswer:
             return True
         else:
             return False

     def build_question(self):
         return f'Вопрос: {self.text}\nСложность {self.diff}/5'

     def build_feedback(self):
         global score
         if self.answer == self.RightAnswer:
             print(f"Ответ верный, получи {self.points} баллов")
             score+=self.points
         else:
             print(f"Ответ неверный, правильный ответ - {self.RightAnswer}")

list_qwest = []
for qwest in list_:
    list_qwest.append(Question(qwest['text'], qwest['diff'], qwest['RightAnswer']))
shuffle(list_qwest)
for qwest in list_qwest:
    print(qwest.build_question())
    qwest.answer = int(input('ans: '))
    qwest.que = True
    #qwest.answer = a
    qwest.build_feedback()
    print('_____________________')
print(f"Вот и всё!\nНабрано баллов: {score}")
