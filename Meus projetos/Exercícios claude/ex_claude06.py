"""
Crie uma classe abstrata Notificador com um método abstrato enviar(mensagem). Implemente NotificadorEmail e NotificadorSMS (cada um imprimindo algo diferente ao "enviar"). Depois crie uma função disparar_notificacoes(notificadores, mensagem) que recebe uma lista de objetos Notificador (de qualquer subtipo) e chama enviar(mensagem) em cada um.
"""
from abc import ABC, abstractmethod 

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensagem):
        print(f'Você recebeu uma mensagem. {mensagem}')

class NotificadorSMS(Notificador):
    def enviar(self, mensagem):
        print(f'Você recebeu um SMS. {mensagem}')

def disparar_notificacoes(notificadores, mensagem):
    for notificador in notificadores:
        notificador.enviar(mensagem)

email = NotificadorEmail()
sms = NotificadorSMS()
lista = [email, sms]

disparar_notificacoes(lista, 'Deseja responder agora?')


#class NotificadorSMS(Notificador):
    #def __init__(self):
        #super().__init__()