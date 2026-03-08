"""
FarmTech Solutions - Módulo de dados
Armazena as listas (vetores) de lavouras cadastradas.
Cada lavoura contém: cultura, nome da fazenda/talhão, dimensões e informações de ruas.
"""

# Lista principal para armazenar os cadastros de lavoura
# Cada elemento é um dicionário com os campos da lavoura
lavouras = []

# Culturas suportadas pelo sistema
CULTURAS_SUPORTADAS = ["café", "milho"]


def obter_lavouras():
    """Retorna a lista de lavouras cadastradas."""
    return lavouras


def adicionar_lavoura(lavoura):
    """Adiciona uma nova lavoura à lista."""
    lavouras.append(lavoura)


def atualizar_lavoura(indice, lavoura):
    """Atualiza a lavoura na posição indicada."""
    if 0 <= indice < len(lavouras):
        lavouras[indice] = lavoura
        return True
    return False


def remover_lavoura(indice):
    """Remove a lavoura na posição indicada."""
    if 0 <= indice < len(lavouras):
        lavouras.pop(indice)
        return True
    return False
