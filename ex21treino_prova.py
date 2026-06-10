def main(n):
    soma = 0

    for i in range(1, n + 1, 2):
        soma = soma + i

    return soma


print(main(9))