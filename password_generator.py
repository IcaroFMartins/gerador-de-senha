import secrets
import string


def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    if tamanho < 4:
        raise ValueError("A senha deve ter pelo menos 4 caracteres.")

    if not caracteres:
        raise ValueError("Selecione pelo menos um tipo de caractere.")

    return "".join(secrets.choice(caracteres) for _ in range(tamanho))


def avaliar_forca(senha):
    pontuacao = 0

    if len(senha) >= 8:
        pontuacao += 1

    if len(senha) >= 12:
        pontuacao += 1

    if any(caractere.islower() for caractere in senha):
        pontuacao += 1

    if any(caractere.isupper() for caractere in senha):
        pontuacao += 1

    if any(caractere.isdigit() for caractere in senha):
        pontuacao += 1

    if any(caractere in string.punctuation for caractere in senha):
        pontuacao += 1

    if pontuacao <= 2:
        return "Fraca"

    if pontuacao <= 4:
        return "Média"

    return "Forte"