from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(item['text'], item['answer']) for item in question_data]

quiz = QuizBrain(question_bank)

while quiz.ainda_tem_perguntas():
    quiz.proxima_pergunta()
print(f"O quiz foi completo \nSua pontuação final foi {quiz.pontuacao}/{quiz.id_pergunta}")

