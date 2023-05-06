from day34questions1 import question_data
from day34questionobject1 import Questionss
from day34quizquestions1 import quizstarter
from day34uipage1 import QuizInterface

a_bank=[]

for ques in question_data:
    q_ques=ques['question']
    q_correct_ans=ques['correct_answer']
    qz_open=Questionss(q_ques,q_correct_ans)#here qz_open is a Questionss object which has 2 attributes
    #text and answer and while text is equated with q_ques,answer attribute will be equated to q_correct
    a_bank.append(qz_open)#and each Questionss object is then appended to list a_bank

quiz=quizstarter(a_bank)
pg=QuizInterface(quiz)

while quiz.questions_left():
    quiz.start_questions()
