from model.missao import Missao
from model.enums import StatusMissao

class MissaoColeta(Missao):
    XP_POR_ITEM = 5

    def __init__(self, nome, descricao, recompensa, quantidade_itens):
        super().__init__(nome, descricao, recompensa)
        self.__quantidade_itens = quantidade_itens

    @property
    def quantidade_itens(self):
        return self.__quantidade_itens

    def calcular_recompensa(self):
        base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return base
        return base + self.quantidade_itens * self.XP_POR_ITEM
