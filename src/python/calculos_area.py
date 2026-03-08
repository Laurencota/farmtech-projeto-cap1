"""
FarmTech Solutions - Cálculos de Área
Funções para calcular a área de plantio das lavouras.
As implementações dos cálculos serão feitas pelos integrantes do grupo.
"""


def calcular_area_retangular(comprimento, largura):
    """
    Calcula a área de plantio para lavouras em formato retangular.

    Usada para a cultura de CAFÉ, que possui comprimento e largura da área.
    A área é obtida multiplicando comprimento pela largura.

    Parâmetros:
        comprimento (float): Comprimento da área em metros.
        largura (float): Largura da área em metros.

    Retorna:
        float: Área em metros quadrados (m²).
              (Implemente: comprimento * largura)

    Exemplo de uso:
        # Dados vindos do cadastro de uma lavoura de café:
        # lavoura = {"comprimento_area": 100, "largura_area": 50, ...}
        area = calcular_area_retangular(
            comprimento=100,
            largura=50
        )
        # Resultado esperado: 5000 m²
    """
    pass


def calcular_area_circular(raio):
    """
    Calcula a área de plantio para lavouras em formato circular (Pivô Central).

    Usada para a cultura de MILHO, que utiliza irrigação por Pivô Central.
    A área é um círculo cujo raio é o raio do pivô.

    Parâmetros:
        raio (float): Raio do pivô em metros.

    Retorna:
        float: Área em metros quadrados (m²).
              (Implemente: use a fórmula da área do círculo: π * raio²)
              (Dica: π pode ser obtido com math.pi ou 3.14159...)

    Exemplo de uso:
        # Dados vindos do cadastro de uma lavoura de milho:
        # lavoura = {"raio_pivo": 400, ...}
        area = calcular_area_circular(raio=400)
        # Resultado esperado: aproximadamente 502.654 m² (se π ≈ 3.14159)
    """
    pass


# =============================================================================
# EXEMPLOS DE USO (comentados - para orientar quem vai implementar)
# =============================================================================
#
# Exemplo 1 - Lavoura de café:
# ----------------
# from dados import lavouras
# lavoura_cafe = lavouras[0]  # assume que a primeira lavoura é de café
# area_cafe = calcular_area_retangular(
#     comprimento=lavoura_cafe["comprimento_area"],
#     largura=lavoura_cafe["largura_area"]
# )
# print(f"Área do café: {area_cafe} m²")
#
#
# Exemplo 2 - Lavoura de milho:
# ----------------
# lavoura_milho = lavouras[1]  # assume que a segunda lavoura é de milho
# area_milho = calcular_area_circular(raio=lavoura_milho["raio_pivo"])
# print(f"Área do milho: {area_milho} m²")
#
#
# Exemplo 3 - Calcular área para qualquer lavoura:
# ----------------
# for lavoura in lavouras:
#     if lavoura["cultura"] == "café":
#         area = calcular_area_retangular(
#             lavoura["comprimento_area"],
#             lavoura["largura_area"]
#         )
#     elif lavoura["cultura"] == "milho":
#         area = calcular_area_circular(lavoura["raio_pivo"])
#     print(f"{lavoura['nome_fazenda']}: {area} m²")
