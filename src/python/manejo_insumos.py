"""
FarmTech Solutions - Manejo de Insumos
Funções para calcular a quantidade de insumos necessários nas lavouras.
As implementações dos cálculos serão feitas pelos integrantes do grupo.
"""


def calcular_insumos_cafe(ml_por_metro, numero_ruas, comprimento_medio_rua):
    """
    Calcula a quantidade total de insumo (em ml) para lavoura de CAFÉ.

    O café é plantado em ruas. O total de metros lineares é obtido
    multiplicando o número de ruas pelo comprimento médio de cada rua.
    A quantidade de insumo é proporcional a esses metros lineares.

    Parâmetros:
        ml_por_metro (float): Mililitros de insumo aplicados por metro linear.
        numero_ruas (int): Número de ruas da lavoura.
        comprimento_medio_rua (float): Comprimento médio de cada rua em metros.

    Retorna:
        float: Quantidade total de insumo em mililitros (ml).
              (Implemente: ml_por_metro * numero_ruas * comprimento_medio_rua)

    Exemplo de uso:
        # Dados vindos do cadastro: 20 ruas de 50m cada, 10 ml por metro
        # lavoura = {"numero_ruas": 20, "comprimento_medio_rua": 50, ...}
        total_ml = calcular_insumos_cafe(
            ml_por_metro=10,
            numero_ruas=20,
            comprimento_medio_rua=50
        )
        # Resultado esperado: 10000 ml (10 litros)
    """
    pass


def calcular_insumos_milho(ml_por_metro, raio_pivo):
    """
    Calcula a quantidade total de insumo (em ml) para lavoura de MILHO.

    O milho usa irrigação por Pivô Central. O pivô gira em um círculo.
    Uma forma de calcular os "metros lineares" é usar a circunferência
    que o pivô percorre em uma volta completa: 2 * π * raio.

    Outra opção: se o insumo for aplicado ao longo do raio em cada passada,
    considerar o raio como referência. O grupo deve definir a regra de negócio.

    Parâmetros:
        ml_por_metro (float): Mililitros de insumo por metro (linear ou da circunferência).
        raio_pivo (float): Raio do pivô em metros.

    Retorna:
        float: Quantidade total de insumo em mililitros (ml).
              (Implemente conforme a regra escolhida pelo grupo.
               Ex.: circunferência = 2 * π * raio_pivo, então
               total_ml = ml_por_metro * circunferência)

    Exemplo de uso:
        # Dados vindos do cadastro de lavoura de milho
        # lavoura = {"raio_pivo": 400, ...}
        total_ml = calcular_insumos_milho(
            ml_por_metro=5,
            raio_pivo=400
        )
        # Se usar circunferência: 2 * 3.14159 * 400 = 2513 m
        # total_ml = 5 * 2513 = 12565 ml
    """
    pass


# =============================================================================
# EXEMPLOS DE USO (comentados - para orientar quem vai implementar)
# =============================================================================
#
# Exemplo 1 - Insumo para lavoura de café:
# ----------------
# from dados import lavouras
# lavoura_cafe = lavouras[0]
# total = calcular_insumos_cafe(
#     ml_por_metro=10,  # 10 ml por metro de rua
#     numero_ruas=lavoura_cafe["numero_ruas"],
#     comprimento_medio_rua=lavoura_cafe["comprimento_medio_rua"]
# )
# print(f"Total de insumo necessário: {total} ml ({total/1000} litros)")
#
#
# Exemplo 2 - Insumo para lavoura de milho:
# ----------------
# lavoura_milho = lavouras[1]
# total = calcular_insumos_milho(
#     ml_por_metro=5,
#     raio_pivo=lavoura_milho["raio_pivo"]
# )
# print(f"Total de insumo necessário: {total} ml")
#
#
# Exemplo 3 - Calcular insumos para qualquer lavoura:
# ----------------
# ml_por_metro_padrao = 8  # valor de exemplo
# for lavoura in lavouras:
#     if lavoura["cultura"] == "café":
#         total = calcular_insumos_cafe(
#             ml_por_metro=ml_por_metro_padrao,
#             numero_ruas=lavoura["numero_ruas"],
#             comprimento_medio_rua=lavoura["comprimento_medio_rua"]
#         )
#     elif lavoura["cultura"] == "milho":
#         total = calcular_insumos_milho(
#             ml_por_metro=ml_por_metro_padrao,
#             raio_pivo=lavoura["raio_pivo"]
#         )
#     print(f"{lavoura['nome_fazenda']} ({lavoura['cultura']}): {total} ml")
