from model.missao import Missao
from model.enums import StatusMissao

class MissaoCaca(Missao):
    XP_POR_INIMIGO = 10

    def __init__(self, nome, descricao, recompensa, quantidade_inimigos):
        super().__init__(nome, descricao, recompensa)
        self.__quantidade_inimigos = quantidade_inimigos

    @property
    def quantidade_inimigos(self):
        return self.__quantidade_inimigos

    def calcular_recompensa(self):
        base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return base
        return base + self.quantidade_inimigos * self.XP_POR_INIMIGO
