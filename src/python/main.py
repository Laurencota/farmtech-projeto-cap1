"""
FarmTech Solutions - Aplicação principal
Sistema de gerenciamento de lavouras - Agricultura Digital.
Ponto de entrada da aplicação.
"""

from menu import exibir_menu, executar_opcao


def main():
    """Executa o loop principal do menu."""
    print("\nBem-vindo ao FarmTech Solutions!")
    print("Sistema de gerenciamento de lavouras (café e milho)")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()
        if not executar_opcao(opcao):
            break


if __name__ == "__main__":
    main()
