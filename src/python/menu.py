"""
FarmTech Solutions - Módulo do menu
Menu interativo para gerenciamento de lavouras.
"""

from dados import (
    lavouras,
    CULTURAS_SUPORTADAS,
    adicionar_lavoura,
    obter_lavouras,
    atualizar_lavoura,
    remover_lavoura,
)


def exibir_menu():
    """Exibe o menu principal da aplicação."""
    print("\n" + "=" * 50)
    print("     FarmTech Solutions - Agricultura Digital")
    print("=" * 50)
    print("1. Inserir dados da lavoura")
    print("2. Mostrar dados cadastrados")
    print("3. Atualizar dados da lavoura")
    print("4. Deletar dados do vetor")
    print("5. Sair do programa")
    print("=" * 50)


def ler_numero(mensagem, tipo=float):
    """Lê um número do usuário, com tratamento de erro."""
    while True:
        try:
            valor = input(mensagem).strip().replace(",", ".")
            return tipo(valor)
        except ValueError:
            print("Valor inválido. Digite um número.")


def inserir_lavoura():
    """Solicita e insere os dados de uma nova lavoura."""
    print("\n--- Inserir dados da lavoura ---")

    # Tipo da cultura
    print(f"Culturas disponíveis: {', '.join(CULTURAS_SUPORTADAS)}")
    cultura = input("Tipo da cultura (café ou milho): ").strip().lower()
    if cultura not in CULTURAS_SUPORTADAS:
        print(f"Cultura inválida. Use uma das opções: {', '.join(CULTURAS_SUPORTADAS)}")
        return

    nome_fazenda = input("Nome da fazenda ou talhão: ").strip()
    if not nome_fazenda:
        print("Nome da fazenda não pode ser vazio.")
        return

    if cultura == "milho":
        # Plantio via Pivô Central
        print("(Plantio via Pivô Central)")
        raio_pivo = ler_numero("Raio do pivô (metros): ")
        lavoura = {
            "cultura": cultura,
            "nome_fazenda": nome_fazenda,
            "raio_pivo": raio_pivo,
        }
    else:
        # café: comprimento, largura, ruas
        comprimento = ler_numero("Comprimento da área (metros): ")
        largura = ler_numero("Largura da área (metros): ")
        numero_ruas = ler_numero("Número de ruas da lavoura: ", int)
        comprimento_medio_rua = ler_numero("Comprimento médio de cada rua (metros): ")
        lavoura = {
            "cultura": cultura,
            "nome_fazenda": nome_fazenda,
            "comprimento_area": comprimento,
            "largura_area": largura,
            "numero_ruas": numero_ruas,
            "comprimento_medio_rua": comprimento_medio_rua,
        }
    adicionar_lavoura(lavoura)
    print("Lavoura cadastrada com sucesso!")


def mostrar_lavouras():
    """Exibe todas as lavouras cadastradas."""
    print("\n--- Dados cadastrados ---")
    if not lavouras:
        print("Nenhuma lavoura cadastrada.")
        return

    for i, lav in enumerate(lavouras):
        print(f"\n[Posição {i}]")
        print(f"  Cultura: {lav['cultura']}")
        print(f"  Fazenda/Talhão: {lav['nome_fazenda']}")
        if lav["cultura"] == "milho":
            print(f"  Raio do pivô (m): {lav['raio_pivo']} (Pivô Central)")
        else:
            print(f"  Comprimento (m): {lav['comprimento_area']}")
            print(f"  Largura (m): {lav['largura_area']}")
            print(f"  Nº de ruas: {lav['numero_ruas']}")
            print(f"  Compr. médio rua (m): {lav['comprimento_medio_rua']}")


def atualizar_lavoura_menu():
    """Atualiza os dados de uma lavoura em determinada posição."""
    print("\n--- Atualizar dados ---")
    if not lavouras:
        print("Nenhuma lavoura cadastrada.")
        return

    indice = ler_numero("Informe a posição para atualizar: ", int)
    if indice < 0 or indice >= len(lavouras):
        print("Posição inválida.")
        return

    print(f"Editando lavoura na posição {indice}...")
    lav_atual = lavouras[indice]

    # Tipo da cultura
    print(f"Culturas disponíveis: {', '.join(CULTURAS_SUPORTADAS)}")
    cultura = input(f"Tipo da cultura [{lav_atual['cultura']}]: ").strip().lower()
    if not cultura:
        cultura = lav_atual["cultura"]
    elif cultura not in CULTURAS_SUPORTADAS:
        print(f"Cultura inválida. Mantendo: {lav_atual['cultura']}")
        cultura = lav_atual["cultura"]

    nome_fazenda = input(f"Nome da fazenda [{lav_atual['nome_fazenda']}]: ").strip()
    nome_fazenda = nome_fazenda or lav_atual["nome_fazenda"]

    try:
        if cultura == "milho":
            if "raio_pivo" in lav_atual:
                raio_pivo = input(f"Raio do pivô (m) [{lav_atual['raio_pivo']}]: ").strip()
                raio_pivo = float(raio_pivo.replace(",", ".")) if raio_pivo else lav_atual["raio_pivo"]
            else:
                raio_pivo = float(input("Raio do pivô (m): ").strip().replace(",", "."))
            nova_lavoura = {
                "cultura": cultura,
                "nome_fazenda": nome_fazenda,
                "raio_pivo": raio_pivo,
            }
        else:
            if "comprimento_area" in lav_atual:
                comprimento = input(f"Comprimento (m) [{lav_atual['comprimento_area']}]: ").strip()
                comprimento = float(comprimento.replace(",", ".")) if comprimento else lav_atual["comprimento_area"]
                largura = input(f"Largura (m) [{lav_atual['largura_area']}]: ").strip()
                largura = float(largura.replace(",", ".")) if largura else lav_atual["largura_area"]
                numero_ruas = input(f"Nº de ruas [{lav_atual['numero_ruas']}]: ").strip()
                numero_ruas = int(numero_ruas) if numero_ruas else lav_atual["numero_ruas"]
                comprimento_medio_rua = input(
                    f"Compr. médio rua (m) [{lav_atual['comprimento_medio_rua']}]: "
                ).strip()
                comprimento_medio_rua = (
                    float(comprimento_medio_rua.replace(",", "."))
                    if comprimento_medio_rua
                    else lav_atual["comprimento_medio_rua"]
                )
            else:
                comprimento = float(input("Comprimento (m): ").strip().replace(",", "."))
                largura = float(input("Largura (m): ").strip().replace(",", "."))
                numero_ruas = int(input("Nº de ruas: ").strip())
                comprimento_medio_rua = float(input("Compr. médio rua (m): ").strip().replace(",", "."))
            nova_lavoura = {
                "cultura": cultura,
                "nome_fazenda": nome_fazenda,
                "comprimento_area": comprimento,
                "largura_area": largura,
                "numero_ruas": numero_ruas,
                "comprimento_medio_rua": comprimento_medio_rua,
            }
    except ValueError:
        print("Valor inválido. Atualização cancelada.")
        return
    if atualizar_lavoura(indice, nova_lavoura):
        print("Dados atualizados com sucesso!")


def deletar_lavoura():
    """Remove uma lavoura do vetor."""
    print("\n--- Deletar dados ---")
    if not lavouras:
        print("Nenhuma lavoura cadastrada.")
        return

    indice = ler_numero("Informe a posição para deletar: ", int)
    if indice < 0 or indice >= len(lavouras):
        print("Posição inválida.")
        return

    if remover_lavoura(indice):
        print("Lavoura removida com sucesso!")


def executar_opcao(opcao):
    """
    Executa a ação correspondente à opção escolhida.
    Retorna False se a opção for Sair, True caso contrário.
    """
    if opcao == "1":
        inserir_lavoura()
    elif opcao == "2":
        mostrar_lavouras()
    elif opcao == "3":
        atualizar_lavoura_menu()
    elif opcao == "4":
        deletar_lavoura()
    elif opcao == "5":
        print("\nEncerrando FarmTech Solutions. Até logo!")
        return False
    else:
        print("Opção inválida. Digite um número de 1 a 5.")
    return True
