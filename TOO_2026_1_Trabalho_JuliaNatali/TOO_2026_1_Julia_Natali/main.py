from model.heroi import Heroi
from model.missao_caca import MissaoCaca
from model.missao_coleta import MissaoColeta
from model.missao_exploracao import MissaoExploracao
from model.enums import ClasseHeroi, StatusMissao

def main():
    heroi = Heroi("Aragorn", ClasseHeroi.GUERREIRO, 100, 100, 15, 8)

    missoes = [
        MissaoCaca("Caça aos Orcs", "derrotar os orcs da floresta", 100, 5),
        MissaoColeta("Ervas Raras", "coletar ervas medicinais", 50, 8),
        MissaoExploracao("Ruínas Antigas", "explorar as ruínas ao norte", 80, 3),
    ]

    print(" Recompensa de cada missão")
    for m in missoes:
        print(f"{m} -> recompensa: {m.calcular_recompensa()}")

    print("\n Ciclo completo até subir de nível")
    print(heroi.exibir_dados())
    for m in missoes:
        print(m.iniciar_missao())
        m.concluir_missao(heroi)
        print(f"{m} -> recompensa paga: {m.calcular_recompensa()}")
    print(heroi.exibir_dados())

    print("Erros de propósito")
    try:
        missoes[0].status = StatusMissao.PENDENTE  # tentando retroceder
    except ValueError as e:
        print("Erro:", e)
    try:
        MissaoCaca("Teste", "teste", 10, 1).concluir_missao(heroi)  # pulando etapa
    except ValueError as e:
        print("Erro:", e)
    try:
        missoes[1].status = "CONCLUIDA"  # string em vez de enum
    except TypeError as e:
        print("Erro:", e)

main()
