import random
import math
import time


#Recozimento Simulado

def fitness_function(individual, values, weights, max_capacity):
    total_value = sum(individual[i] * values[i] for i in range(len(individual)))
    total_weight = sum(individual[i] * weights[i] for i in range(len(individual)))

    if total_weight > max_capacity:
        # Penalizar indivíduos que excedem a capacidade máxima da mochila
        fitness = 0
    else:
        fitness = total_value

    return fitness

def knapsack_sa(values, weights, max_capacity, initial_temperature, cooling_rate, num_iterations):
    start_time = time.time()

    num_items = len(values)
    current_solution = [random.randint(0, 1) for _ in range(num_items)]
    best_solution = current_solution.copy()

    current_fitness = fitness_function(current_solution, values, weights, max_capacity)
    best_fitness = current_fitness

    temperature = initial_temperature

    for iteration in range(num_iterations):
        neighbor_solution = current_solution.copy()
        index = random.randint(0, num_items - 1)
        neighbor_solution[index] = 1 - neighbor_solution[index]  # Inverte um item aleatório

        neighbor_fitness = fitness_function(neighbor_solution, values, weights, max_capacity)

        if neighbor_fitness > current_fitness:
            current_solution = neighbor_solution
            current_fitness = neighbor_fitness
        else:
            acceptance_probability = math.exp((neighbor_fitness - current_fitness) / temperature)
            if random.random() < acceptance_probability:
                current_solution = neighbor_solution
                current_fitness = neighbor_fitness

        if current_fitness > best_fitness:
            best_solution = current_solution
            best_fitness = current_fitness

        temperature *= cooling_rate
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução: ", execution_time, "segundos")
    return best_solution

# Exemplo de uso
values_backpack = [60, 100, 120]
weights_backpack = [10, 20, 30]
max_capacity_backpack = 40

initial_temperature_backpack = 100.0
cooling_rate_backpack = 0.95
num_iterations_backpack = 1000

best_solution = knapsack_sa(values_backpack, weights_backpack, max_capacity_backpack, initial_temperature_backpack, cooling_rate_backpack, num_iterations_backpack)
total_value = sum(best_solution[i] * values_backpack[i] for i in range(len(best_solution)))
total_weight = sum(best_solution[i] * weights_backpack[i] for i in range(len(best_solution)))

print("Melhor solução encontrada:")
print(best_solution)
print("Valor total: ", total_value)
print("Peso total: ", total_weight)
