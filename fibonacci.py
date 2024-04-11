def fibonacci_ate_n(N):
    a, b = 0, 1
    while a <= N:
        print(a, end=' ')
        a, b = b, a + b

while True:
    try:
        entrada = input("Digite um número inteiro positivo N (ou 'q' para sair): ")
        if entrada.lower() == 'q':
            break
        
        N = int(entrada)
        
        if N <= 0:
            print("Por favor, digite um número inteiro positivo.")
            continue
        
        print("Sequência de Fibonacci até o imediatamente superior a N:")
        fibonacci_ate_n(N)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro positivo ou 'q' para sair.")
