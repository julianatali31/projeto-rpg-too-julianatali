from model.missao import Missao
from model.enums import StatusMissao

class MissaoExploracao(Missao):
    XP_POR_AREA = 20

    def __init__(self, nome, descricao, recompensa, areas_exploradas):
        super().__init__(nome, descricao, recompensa)
        self.__areas_exploradas = areas_exploradas

    @property
    def areas_exploradas(self):
        return self.__areas_exploradas

    def calcular_recompensa(self):
        base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return base
        return base + self.areas_exploradas * self.XP_POR_AREA
