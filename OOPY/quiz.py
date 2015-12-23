import datetime
import random

from questions import Add, Multiply

# Expand the script so that:
#
# You can vary the number of questions
# You can change the range of numbers
# Add Subtraction questions

class Quiz:
    questions =[]
    answers = []
    
    def __init__(self):
        question_types = (Add, Multiply)
        question_types[0](1,5)
        # generate 10 random questions with numbers from 1 to 10
        for _ in range(10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            question = random.choice(question_types)(num1, num2)
            # add these question into self.question
            self.questions.append(question)
        
        
    def take_quiz(self):
        # log the start time
        # ask all of the questions
        # log if they got the question right
        # log the end time
        # show a summary
        pass
    
    def ask(self, question):
        # log tbe start time
        # capture answer
        # check the answer
        # log the end time
        # if answer's right, send back True
        # otherwise, send back False
        # send back the elapsed time, too
        pass
    
    def total_correct(self):
        # return total correct answers
        total = 0
        for ans in self.answers:
            if ans[0]:
                total += 1
        return total

    def summary(self):
        # print no. of right and worng answers from total # of questions
        # total time used
        print( "You got {} / {} right ". format(
         self.total_correct(),
         len(self.questions)
        ))
        
        print("It took you {} seconds total.".format(
            (self.end_time - self.start_time).seconds
        ))