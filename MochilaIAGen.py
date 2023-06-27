import random
import time

def generate_individual(num_items):
    """
    Função para gerar um indivíduo aleatório para o problema da mochila.

    Argumentos:
    - num_items: O número total de itens da mochila.

    Retorna:
    Um vetor binário representando a presença (1) ou ausência (0) de cada item na mochila.
    """

    # Cria um vetor de tamanho num_items usando list comprehension
    # Em cada posição do vetor, atribui um valor aleatório de 0 ou 1 usando random.randint(0, 1)
    # O valor 1 indica que o item está presente e o valor 0 indica que o item está ausente na mochila
    return [random.randint(0, 1) for _ in range(num_items)]

def generate_population(population_size, num_items):
    """
    Função para gerar uma população inicial de indivíduos aleatórios para o problema da mochila.

    Argumentos:
    - population_size: O tamanho da população desejada.
    - num_items: O número total de itens da mochila.

    Retorna:
    Uma lista contendo a população inicial de indivíduos, onde cada indivíduo é representado por um vetor binário.
    """

    # Utiliza list comprehension para criar uma lista com population_size indivíduos
    # Cada indivíduo é gerado chamando a função generate_individual(num_items)
    # Assim, cada indivíduo é um vetor binário representando a presença (1) ou ausência (0) de cada item na mochila
    return [generate_individual(num_items) for _ in range(population_size)]

def fitness_function(individual, values, weights, max_capacity):
    """
    Função de avaliação (fitness) para medir a aptidão de um indivíduo na resolução do problema da mochila.

    Argumentos:
    - individual: O vetor binário representando um indivíduo (solução).
    - values: Uma lista dos valores de cada item da mochila.
    - weights: Uma lista dos pesos de cada item da mochila.
    - max_capacity: A capacidade máxima da mochila.

    Retorna:
    O valor da aptidão (fitness) do indivíduo, representando a soma dos valores dos itens ou zero se a capacidade máxima for excedida.
    """

    # Calcula o valor total somando o produto do valor de cada item com sua presença (1) ou ausência (0) na mochila
    total_value = sum(individual[i] * values[i] for i in range(len(individual)))

    # Calcula o peso total somando o produto do peso de cada item com sua presença (1) ou ausência (0) na mochila
    total_weight = sum(individual[i] * weights[i] for i in range(len(individual)))

    if total_weight > max_capacity:
        # Se o peso total exceder a capacidade máxima da mochila, penaliza o indivíduo atribuindo uma aptidão de zero
        fitness = 0
    else:
        # Caso contrário, a aptidão é igual ao valor total
        fitness = total_value

    return fitness


def roulette_wheel_selection(population, fitness_values):
    """
    Função de seleção por roleta para escolher indivíduos da população com base em suas aptidões.

    Argumentos:
    - population: A população atual de indivíduos.
    - fitness_values: Uma lista contendo as aptidões (valores fitness) correspondentes a cada indivíduo.

    Retorna:
    Uma lista contendo dois indivíduos selecionados aleatoriamente com base em suas aptidões proporcionais.
    """

    # Calcula a soma total das aptidões de toda a população
    total_fitness = sum(fitness_values)

    # Calcula as probabilidades de seleção para cada indivíduo, proporcional às suas aptidões
    selection_probs = [fitness / total_fitness for fitness in fitness_values]

    # Realiza a seleção aleatória de dois indivíduos da população usando as probabilidades de seleção como pesos
    selected_individuals = random.choices(population, weights=selection_probs, k=2)

    return selected_individuals


def crossover(parent1, parent2):
    """
    Função de cruzamento (recombinação) para gerar descendentes a partir de dois indivíduos pais.

    Argumentos:
    - parent1: O primeiro indivíduo pai.
    - parent2: O segundo indivíduo pai.

    Retorna:
    Uma tupla contendo os dois descendentes gerados a partir dos pais.
    """

    # Escolhe aleatoriamente um ponto de corte para a recombinação
    crossover_point = random.randint(1, len(parent1) - 1)

    # Realiza o cruzamento dos pais no ponto de corte
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2


def mutation(individual, mutation_rate):
    """
    Função de mutação para introduzir alterações aleatórias em um indivíduo.

    Argumentos:
    - individual: O indivíduo a ser mutado.
    - mutation_rate: A taxa de mutação, que determina a probabilidade de ocorrer uma mutação em cada posição do indivíduo.

    Retorna:
    O indivíduo mutado.
    """

    # Cria uma cópia do indivíduo original para evitar modificar o indivíduo original
    mutated_individual = individual.copy()

    # Percorre cada posição do indivíduo e verifica se ocorrerá uma mutação
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            mutated_individual[i] = 1 - mutated_individual[i]  # Inverte o valor

    return mutated_individual

def next_generation(population, values, weights, max_capacity, mutation_rate):
    """
    Função para gerar a próxima geração da população utilizando seleção, cruzamento e mutação.

    Argumentos:
    - population: A população atual de indivíduos.
    - values: Uma lista dos valores de cada item da mochila.
    - weights: Uma lista dos pesos de cada item da mochila.
    - max_capacity: A capacidade máxima da mochila.
    - mutation_rate: A taxa de mutação.

    Retorna:
    A nova geração da população, respeitando o tamanho da população original.
    """

    new_population = []

    # Continua gerando indivíduos até que a nova população tenha o mesmo tamanho da população original
    while len(new_population) < len(population):
        # Seleciona dois pais utilizando o método da roleta
        parent1, parent2 = roulette_wheel_selection(population, [fitness_function(individual, values, weights, max_capacity) for individual in population])

        # Realiza o cruzamento entre os pais para gerar dois descendentes
        child1, child2 = crossover(parent1, parent2)

        # Aplica a mutação nos descendentes gerados
        mutated_child1 = mutation(child1, mutation_rate)
        mutated_child2 = mutation(child2, mutation_rate)

        # Adiciona os descendentes mutados à nova população
        new_population.extend([mutated_child1, mutated_child2])

    # Retorna a nova população respeitando o tamanho da população original
    return new_population[:len(population)]


def genetic_algorithm(values, weights, max_capacity, population_size, mutation_rate, num_iterations):
    """
    Função do algoritmo genético para resolver o problema da mochila.

    Argumentos:
    - values: Uma lista dos valores de cada item da mochila.
    - weights: Uma lista dos pesos de cada item da mochila.
    - max_capacity: A capacidade máxima da mochila.
    - population_size: O tamanho da população.
    - mutation_rate: A taxa de mutação.
    - num_iterations: O número de iterações do algoritmo genético.

    Retorna:
    Uma tupla contendo o melhor indivíduo encontrado e sua aptidão (valor total da mochila).
    """
    start_time = time.time()
    num_items = len(values)

    # Gera a população inicial
    population = generate_population(population_size, num_items)

    best_fitness = 0
    best_individual = None

    # Executa o algoritmo genético por um número de iterações definido
    for _ in range(num_iterations):
        # Calcula as aptidões (valores fitness) de cada indivíduo na população
        fitness_values = [fitness_function(individual, values, weights, max_capacity) for individual in population]

        # Obtém o índice do melhor indivíduo na população
        best_index = fitness_values.index(max(fitness_values))

        # Atualiza o melhor fitness e o melhor indivíduo encontrado, se necessário
        if fitness_values[best_index] > best_fitness:
            best_fitness = fitness_values[best_index]
            best_individual = population[best_index]

        # Gera a próxima geração da população
        population = next_generation(population, values, weights, max_capacity, mutation_rate)
    
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução: ", execution_time, "segundos")

    # Retorna o melhor indivíduo encontrado e sua aptidão
    return best_individual, best_fitness


values_backpack = [60, 100, 120]
weights_backpack = [10, 20, 30]
max_capacity_backpack = 40

population_size_backpack = 100
mutation_rate_backpack = 0.1
num_iterations_backpack = 100

best_individual, best_fitness = genetic_algorithm(values_backpack, weights_backpack, max_capacity_backpack, population_size_backpack, mutation_rate_backpack, num_iterations_backpack)

print("Melhor indivíduo:", best_individual)
print("Melhor aptidão:", best_fitness)
