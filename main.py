from password_generator import avaliar_forca, gerar_senha


def perguntar_sim_nao(mensagem):
    resposta = input(f"{mensagem} (s/n): ").strip().lower()
    return resposta == "s"


def main():
    print("=" * 30)
    print("Gerador de Senhas")
    print("=" * 30)

    try:
        tamanho = int(input("Tamanho da senha [padrão: 12]: ") or 12)

        usar_maiusculas = perguntar_sim_nao("Incluir letras maiúsculas?")
        usar_numeros = perguntar_sim_nao("Incluir números?")
        usar_simbolos = perguntar_sim_nao("Incluir símbolos?")

        senha = gerar_senha(
            tamanho=tamanho,
            usar_maiusculas=usar_maiusculas,
            usar_numeros=usar_numeros,
            usar_simbolos=usar_simbolos,
        )

        print("\nSenha gerada:")
        print(senha)
        print(f"Força estimada: {avaliar_forca(senha)}")

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()