import html
class quizstarter:
    def __init__(self,lister):
        self.questionno=0
        self.current_question=None
        self.score=0
        self.listerr=lister
    def questions_left(self):

        return self.questionno < len(self.listerr)
            # return True
    def start_questions(self):
        self.current_question=self.listerr[self.questionno]
        self.questionno+=1
        q_text=html.unescape(self.current_question.text)
        return f"Q.{self.questionno} {q_text}"
        # user_ans=input(f"{self.questionno}.{q_text}?True or False:")
        # self.checkans(user_ans)
    def checkans(self,user_ans):
        if user_ans.lower()==self.current_question.answer.lower():
            self.score+=1
            return True
            # print(f"Correct:your score is {self.score}/{self.questionno}")
        else:
            return False
            # print(f"Wrong:Your score is {self.score}/{self.questionno}")



        