print("Hello world with Python!");

class Question:
    def __init__(self, id, title, options ,answer):
        self.id = id
        self.title =  title;
        self.options = options
        self.answer = answer




question_1_options =  "a)Ada\nb)John\nc)Thomas"
question_2_options =  "a)Billy kimber\nb)Luca Changreta\nc)Sabini"
question_3_options =  "a)Esme\nb)Grace\nc)Ada"


points = 0

question1 = Question(1, "Which one is  the oldest of Shelbys brothers?",question_1_options ,'b')
question2 = Question(2, "Italian enemy of the fourth season",question_2_options ,'b')
question3 = Question(3, "Name of Johns wife",question_3_options ,'a')

questions = []
questions.append(question1)
questions.append(question2)
questions.append(question3)

def verifyAnswer(question, userAnswer):
    if(question.answer == userAnswer):
        return True
    else:
        return False


for question in questions:
    print(question.title)
    print(question.options+"")
    userAnswer = input("Your Answer: ")
    if(verifyAnswer(question ,userAnswer)):
        print("Correct answer!")
        points += 1
    else:
        print("Incorrect answer, sorry!")

print("Total points: " +str(points))




