class QuizBrain():
     def __init__(self, lista_perguntas):
         self.id_pergunta = 0
         self.lista_perguntas = lista_perguntas
         self.pontuacao = 0

     def ainda_tem_perguntas(self):
         return self.id_pergunta < len(self.lista_perguntas)


     def proxima_pergunta(self):
         pergunta_atual = self.lista_perguntas[self.id_pergunta]
         self.id_pergunta += 1
         resposta_usuario = input(f"{self.id_pergunta}: {pergunta_atual.pergunta}. (True/False)? ")
         self.checa_resposta(resposta_usuario, pergunta_atual.resposta)


     def checa_resposta(self, resposta_usuario, resposta_certa):
         if resposta_usuario.lower() == resposta_certa.lower():
             print("ACERTOUUUU!!")
             self.pontuacao += 1
         else:
             print("Errou :(")
         print(f"Sua pontuação é igual a {self.pontuacao}/{self.id_pergunta}")
         print("\n")

