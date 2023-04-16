import random

def f(x):
  # Define a função a ser otimizada
  return x**2

def calcularAptidao(individuo):
  # Calcula o valor de aptidão para um indivíduo
  return -f(individuo[0])

def cruzar(pai1, pai2):
  # Realiza o cruzamento entre dois pais
  filho = [(pai1[0] + pai2[0]) / 2]
  return filho

def realizarMutacao(individuo, taxa_mutacao):
  # Realiza a mutação em um indivíduo
  if random.random() < taxa_mutacao:
    individuo[0] = individuo[0] + random.uniform(-0.5, 0.5)
    # Mantém o indivíduo dentro do intervalo [-5, 5]
    individuo[0] = min(max(individuo[0], -5), 5)
  return individuo

def criarIndividuo():
  # Cria um novo indivíduo com um valor aleatório de x
  return [random.uniform(-5, 5)]

def criarPopulacao(tamanho):
  # Cria uma nova população de indivíduos
  return [criarIndividuo() for _ in range(tamanho)]

def selecionarPais(populacao):
  # Seleciona dois pais aleatórios com base na roleta
  somaAptidao = sum([calcularAptidao(individuo) for individuo in populacao])
  probabilidadeSelecao = [
    calcularAptidao(individuo) / somaAptidao for individuo in populacao
  ]
  pai1 = random.choices(populacao, weights=probabilidadeSelecao)[0]
  pai2 = random.choices(populacao, weights=probabilidadeSelecao)[0]
  return pai1, pai2

def algoritmoGenetico(tamanhoPopulacao, taxaMutacao, quantidadeGeracoes):
  # Executa o algoritmo genético
  populacao = criarPopulacao(tamanhoPopulacao)
  for i in range(quantidadeGeracoes):
    # Seleciona pais, realiza cruzamento e mutação, e cria uma nova população
    novaPopulacao = []
    for _ in range(tamanhoPopulacao):
      pai1, pai2 = selecionarPais(populacao)
      filho = cruzar(pai1, pai2)
      filho = realizarMutacao(filho, taxaMutacao)
      novaPopulacao.append(filho)
    populacao = novaPopulacao
    # Imprime o valor de aptidão do melhor indivíduo da geração atual
    melhorIndividuo = max(populacao, key=calcularAptidao)
    print(
      "Geração {}: Valor de aptidão = {} \nMelhor indivíduo da população = {}\n".format(
        i + 1, calcularAptidao(melhorIndividuo), melhorIndividuo[0])
    )
  # Retorna o melhor indivíduo da população final
  return max(populacao, key=calcularAptidao)

# Define os parâmetros do algoritmo genético
tamanhoPopulacao = 50
taxaMutacao = 0.1
quantidadeGeracoes = 7

# Executa o algoritmo genético
melhorIndividuo = algoritmoGenetico(tamanhoPopulacao, taxaMutacao, quantidadeGeracoes)

# Imprime o resultado final
print("Melhor indivíduo encontrado: {}".format(melhorIndividuo[0]))
print("Valor de aptidão: {}".format(calcularAptidao(melhorIndividuo)))
