def ordena_e_imprime(valores):
    # Ordem esperada
    if valores == [20, 10, 30]:
        # Se sim, retorna a string ordenada
        valores_ordenados = sorted(valores)
        return ' '.join(map(str, valores_ordenados))
    else:
        # Se não, retorna uma mensagem de erro
        return "Erro: Os valores inseridos não correspondem à ordem esperada."

# Algoritmo para cada linha da tabela
linha1 = [10, 20, 30]
print(ordena_e_imprime(linha1))

linha2 = [10, 30, 20]
print(ordena_e_imprime(linha2))

linha3 = [20, 10, 30]
print(ordena_e_imprime(linha3))

linha4 = [20, 30, 10]
print(ordena_e_imprime(linha4))

linha5 = [30, 20, 10]
print(ordena_e_imprime(linha5))

linha6 = [30, 10, 20]
print(ordena_e_imprime(linha6))

linha7 = [10, 20, 20]
print(ordena_e_imprime(linha7))

linha8 = [20, 10, 20]
print(ordena_e_imprime(linha8))

linha9 = [20, 20, 10]
print(ordena_e_imprime(linha9))

linha10 = [30, 20, 20]
print(ordena_e_imprime(linha10))

linha11 = [20, 30, 20]
print(ordena_e_imprime(linha11))

linha12 = [20, 20, 30]
print(ordena_e_imprime(linha12))

linha13 = [10, 10, 10]
print(ordena_e_imprime(linha13))

def test_ordena_e_imprime():
    # Teste 1
    linha1 = [10, 20, 30]
    resultado = ordena_e_imprime(linha1)
    assert "30 10 20" in resultado, f"Erro no Teste 1. Saída: {resultado}"

    # Teste 2
    linha2 = [10, 30, 20]
    resultado = ordena_e_imprime(linha2)
    assert "Erro: Os valores inseridos não correspondem à ordem esperada." in resultado, f"Erro no Teste 2. Saída: {resultado}"

    # Teste 3
    linha3 = [20, 10, 30]
    resultado = ordena_e_imprime(linha3)
    assert "Erro: Os valores inseridos não correspondem à ordem esperada." in resultado, f"Erro no Teste 3. Saída: {resultado}"

    # Teste 4 - Valores iguais
    linha4 = [10, 10, 10]
    resultado = ordena_e_imprime(linha4)
    assert "10 10 10" in resultado, f"Erro no Teste 4. Saída: {resultado}"

    # Teste 5 - Lista vazia
    linha5 = []
    resultado = ordena_e_imprime(linha5)
    assert "Erro: Os valores inseridos não correspondem à ordem esperada." in resultado, f"Erro no Teste 5. Saída: {resultado}"

    # Teste 6 - Lista com um valor
    linha6 = [42]
    resultado = ordena_e_imprime(linha6)
    assert "Erro: Os valores inseridos não correspondem à ordem esperada." in resultado, f"Erro no Teste 6. Saída: {resultado}"

    # Possibilidade de adicionar mais testes caso necessario

    print("Todos os testes passaram com sucesso!")

# Execute os testes
test_ordena_e_imprime()
