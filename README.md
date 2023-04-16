# Algoritmo genético

Exemplo de algoritmo genético escrito na linguagem Python que tem como objetivo otimizar funções matemáticas utilizando conceitos de genética. O programa encontra o valor mínimo da função f(x) = x^2 (poderia ser qualquer outra função) para x no intervalo entre –5 e 5 (o intervalo também pode ser modificado).

## 📖 Descrição

O código é um exemplo de algoritmo genético em Python pois ele utiliza conceitos de evolução, cruzamento e mutação para encontrar o melhor mínimo para a função. 

Nesse exemplo é utilizada a função f(x) = x2^, o algoritmo usa uma população de soluções candidatas (chamadas de indivíduos) para encontrar uma solução considerada ótima. Ele funciona de forma iterativa, gerando novas gerações de indivíduos a partir dos indivíduos com maior aptidão da geração anterior, cada geração com soluções potencialmente melhores. 

O código foi dividido em várias funções para deixar mais organizado. Irei detalhar todas essas funções a seguir:
- **f(x)**: É a função que será otimizada, no exemplo acima foi utilizada a função f(x) = x2 , mas ela pode ser substituída por uma outra função; 
- **calcularAptidao(individuo)**: Calcula o valor de aptidão para um indivíduo. Esse valor representa a qualidade do indivíduo na resolução do problema; 
- **cruzar(pa1, pai2)**: Realiza o cruzamento entre dois indivíduos, gerando um filho que combina as características deles, essa combinação é feita calculando a média de valores X dos pais; 
- **realizarMutacao(individuo, taxa_mutacao)**: Realiza a mutação em um indivíduo variando o valor de X dele. Essa variação é controlada pela variável “taxa_variacao”, a mutação é feita adicionando um valor aleatório entre –0,5 e 0,5 ao valor de X do indivíduo; 
- **criarIndividuo()**: Cria um novo indivíduo com um valor de X aleatório entre –5 e 5 (esse intervalo também pode ser alterado dependendo do caso que se deseja testar); 
- **criarPopulacao(tamanho)**: Cria uma população de indivíduos chamando a função “criarIndividuo” várias vezes dependendo do valor da variável “tamanho”; 
- **selecionarPais(populacao)**: Seleciona dois indivíduos que serão utilizados no cruzamento, essa seleção é aleatória, mas tem como base a aptidão do indivíduo, os que tiverem uma melhor aptidão, terão uma maior probabilidade de serem escolhidos. 
- **algoritmoGenetico(tamanhoPopulacao, taxaMutacao, quantidadeGeracoes)**: Essa é a função principal, ela chama todas as outras funções, executando o programa como um todo. Ela recebe o tamanho da população, a taxa de mutação e a quantidade de gerações, realiza todas as iterações e retorna o melhor indivíduo da última geração.

## 🚀 Como executar o programa

- Fazer o clone do projeto ou o download dele
- Acessar a pasta do projeto e abri-lo no editor de código de sua preferência
- Alterar os valores das variáveis das linhas 54, 65 e 66 (opcional)
```python
tamanhoPopulacao  =  50
taxaMutacao  =  0.1
quantidadeGeracoes  =  10
``` 
- Executar o seguinte comando no terminal:
```
python main.py
```

Feito com 💜 por Tiago Lopes