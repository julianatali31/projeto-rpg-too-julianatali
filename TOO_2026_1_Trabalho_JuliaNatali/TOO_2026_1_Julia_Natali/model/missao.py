from model.enums import StatusMissao

# Encapsulamento: todos os atributos sao privados e tem property para leitura
# Setter so existe para o status, porque ele muda durante o jogo, e mesmo assim
# valida a sequencia PENDENTE -> EM_ANDAMENTO -> CONCLUIDA. Nome, descricao e
# recompensa definem a missao e nao mudam depois de criada, entao ficam sem setter.
class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = StatusMissao.PENDENTE

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def recompensa(self):
        return self.__recompensa

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if not isinstance(novo_status, StatusMissao):
            raise TypeError("O status precisa ser um StatusMissao")
        sequencia = list(StatusMissao)
        posicao_atual = sequencia.index(self.__status)
        posicao_nova = sequencia.index(novo_status)
        if posicao_nova != posicao_atual + 1:
            raise ValueError(
                f"Transição inválida: {self.__status.value} -> {novo_status.value}"
            )
        self.__status = novo_status

    def iniciar_missao(self):
        self.status = StatusMissao.EM_ANDAMENTO
        return f"A missão {self.nome} começou! O objetivo é {self.descricao}."

    def calcular_recompensa(self):
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        return self.recompensa

    def concluir_missao(self, heroi):
        # primeiro conclui, depois paga: a recompensa so vale com status CONCLUIDA
        self.status = StatusMissao.CONCLUIDA
        heroi.ganhar_experiencia(self.calcular_recompensa())

    def exibir_dados(self):
        msg = f'''
[{self.__class__.__name__}]
Nome: {self.nome}
Descrição: {self.descricao}
Recompensa: {self.recompensa}
Status: {self.status.value}
'''
        return msg

    def __str__(self):
        return f'missão [{self.__class__.__name__}]: {self.nome} | status: {self.status.value}'
