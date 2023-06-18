import random
from typing import List
import time
from xml.etree import ElementTree as ET
import sys

class OligoNode:
    def __init__(self, olig: str, index: int, matches: int):
        self.olig = olig
        self.index = index
        self.matches = matches

oligo_nodes = []

def append_oligs(begin_index: int) -> List[int]:
    result_list = []
    for i in range(len(oligo_nodes)):
        for j in range(oligo_nodes[i].matches):
            result_list.append(i)
        if i == begin_index and result_list:
            result_list.pop()
    return result_list


class DNA_Chain:
    def __init__(self):
        self.result = ""
        self.fit = 0
        self.used_nodes = []
    
    def __len__(self):
        return len(self.result)

    def calc_fitness_score(self, oligo_nodes, probe, match_weight=20):
        self.fit = 0
        for i in range(1, len(self.used_nodes)):
            match_score = 0
            for j in range(probe - 1):
                if oligo_nodes[self.used_nodes[i]].olig[j] == oligo_nodes[self.used_nodes[i - 1]].olig[probe - 1 - j]:
                    match_score += 1
                else:
                    break
            self.fit += match_score * match_weight - (probe - match_score)

    def combine_oligs(self, probe: int, desired_length: int):
        self.result = ""
        self.result += oligo_nodes[self.used_nodes[0]].olig
        for i in range(1, len(self.used_nodes)):
            overlap = 0
            for j in range(probe - 1):
                if oligo_nodes[self.used_nodes[i]].olig[j] != oligo_nodes[self.used_nodes[i - 1]].olig[probe - 1 - j]:
                    break
                overlap += 1
            to_add = oligo_nodes[self.used_nodes[i]].olig[overlap:]
            if len(self.result) + len(to_add) > desired_length:
                to_add = to_add[:desired_length - len(self.result)]
            self.result += to_add



    def randomize(self, begin_index: int):
        to_add = append_oligs(begin_index)
        self.used_nodes.append(oligo_nodes[begin_index].index)
        while to_add:
            next = random.randint(0, len(to_add) - 1)
            self.used_nodes.append(to_add[next])
            to_add.pop(next)

    def cross_nodes(self, parent1, parent2):
        self.used_nodes.clear()

        length = min(len(parent1.used_nodes), len(parent2.used_nodes))

        point1 = random.randint(0, length - 1)
        point2 = random.randint(point1, length - 1)
        
        for i in range(length):
            if point1 < i <= point2:
                self.used_nodes.append(parent2.used_nodes[i])
            else:
                self.used_nodes.append(parent1.used_nodes[i])


        nodes_copy = oligo_nodes.copy()
        oligs_to_replace = []
        oligs_replacement = []

        for i in range(len(self.used_nodes)):
            if nodes_copy[self.used_nodes[i]].matches > 0:
                nodes_copy[self.used_nodes[i]].matches -= 1
            else:
                oligs_to_replace.append(i)

        for i in range(len(nodes_copy)):
            for j in range(nodes_copy[i].matches):
                oligs_replacement.append(i)

        if len(oligs_replacement) == len(oligs_to_replace):
            for i in range(len(oligs_to_replace)):
                self.used_nodes[oligs_to_replace[i]] = oligs_replacement[i]

def convert_intensity(intensity: int) -> int:
    if intensity == 0:
        return 0
    elif intensity in (1, 2):
        return 1
    elif intensity == 3:
        return random.randint(1,2)
    elif intensity == 4:
        return 2
    elif intensity == 5:
        return random.randint(2,3)
    elif intensity in (8, 9):
        return random.randint(7, 8)
    elif intensity in (6, 7, 8):
        return random.randint(4, 6)  
    elif intensity >= 9:
        return 9  

final_result = ""
total_nodes = 0


def main_algorithm(begin_index, probe, length, best_population_percentage, iterations, mutation_chance):
    population_size = 100
    num_of_mutations = length // 100
    best_population_size = (population_size * best_population_percentage) // 100
    population = []
    best_fitness_list = [0] * best_population_size
    indexes_of_best_list = [0] * best_population_size
    best_in_last_generations = [0] * iterations
    mutations_in_generation = (population_size * mutation_chance) // 100

    for i in range(population_size):
        one = DNA_Chain()
        one.randomize(begin_index)
        one.combine_oligs(probe, length)
        one.calc_fitness_score(oligo_nodes, probe)
        population.append(one)
        if i < best_population_size:
            if i == 0:
                best_fitness_list[i] = one.fit
                indexes_of_best_list[i] = i
            else:
                for j in range(i):
                    if one.fit > best_fitness_list[j]:
                        for k in range(i, j - 1, -1):
                            if k < best_population_size - 1:
                                best_fitness_list[k + 1] = best_fitness_list[k]
                                indexes_of_best_list[k + 1] = indexes_of_best_list[k] 
                        best_fitness_list[j] = one.fit
                        indexes_of_best_list[j] = i
                        break
        else:
            for j in range(best_population_size):
                if one.fit > best_fitness_list[j]:
                    for k in range(best_population_size - 2, j - 1, -1):
                        best_fitness_list[k + 1] = best_fitness_list[k]
                        indexes_of_best_list[k + 1] = indexes_of_best_list[k]
                    best_fitness_list[j] = one.fit
                    indexes_of_best_list[j] = i
                    break

    elitism_number = int(best_population_size * 0.05) 

    for population_iter in range(iterations):
        mutation_counter = 0
        elites = sorted(population, key=lambda x: x.fit, reverse=True)[:elitism_number]
        
        for i in range(elitism_number, population_size):
            prevent_ineffective_mutation = i in indexes_of_best_list if indexes_of_best_list != len(indexes_of_best_list) - 1 else False
            if not prevent_ineffective_mutation:
                if mutation_counter >= mutations_in_generation:
                    parent1 = random.randint(0, best_population_size - 1)
                    parent2 = random.randint(0, best_population_size - 1)
                    while parent2 == parent1:
                        parent2 = random.randint(0, best_population_size - 1)
                    population[i].cross_nodes(population[indexes_of_best_list[parent1]], population[indexes_of_best_list[parent2]])
                    population[i].combine_oligs(probe, length)
                    population[i].calc_fitness_score(oligo_nodes, probe)
                else:
                    parent1 = random.randint(0, best_population_size - 1)
                    parent2 = random.randint(0, best_population_size - 1)
                    while parent2 == parent1:
                        parent2 = random.randint(0, best_population_size - 1)
                    population[i].cross_nodes(population[indexes_of_best_list[parent1]], population[indexes_of_best_list[parent2]])
                    for _ in range(num_of_mutations):
                        index1, index2 = random.randint(0, len(population[i].used_nodes) - 1), random.randint(0, len(population[i].used_nodes) - 1)
                        temp = population[i].used_nodes[index2]
                        population[i].used_nodes[index2] = population[i].used_nodes[index1]
                        population[i].used_nodes[index1] = temp
                    population[i].combine_oligs(probe, length)
                    population[i].calc_fitness_score(oligo_nodes, probe)
                    mutation_counter += 1
                    
        population[:elitism_number] = elites

        for i in range(population_size):
            prevent_ineffective_mutation = i in indexes_of_best_list if indexes_of_best_list != len(indexes_of_best_list) - 1 else False
            if not prevent_ineffective_mutation:
                for j in range(best_population_size):
                    if population[i].fit > best_fitness_list[j]:
                        for k in range(best_population_size - 2, j - 1, -1):
                            best_fitness_list[k + 1] = best_fitness_list[k]
                            indexes_of_best_list[k + 1] = indexes_of_best_list[k]
                        best_fitness_list[j] = population[i].fit
                        indexes_of_best_list[j] = i
                        break
        best_in_last_generations[iterations - population_iter - 1] = best_fitness_list[0]

    while best_in_last_generations[0] != best_in_last_generations[iterations - 1]:
        mutation_counter = 0
        for i in range(population_size):
            prevent_ineffective_mutation = i in indexes_of_best_list if indexes_of_best_list != len(indexes_of_best_list) - 1 else False
            if not prevent_ineffective_mutation:
                if mutation_counter >= mutations_in_generation:
                    parent1 = random.randint(0, best_population_size - 1)
                    parent2 = random.randint(0, best_population_size - 1)
                    while parent2 == parent1:
                        parent2 = random.randint(0, best_population_size - 1)
                    population[i].cross_nodes(population[indexes_of_best_list[parent1]], population[indexes_of_best_list[parent2]])
                    population[i].combine_oligs(probe, length)
                    population[i].calc_fitness_score(oligo_nodes, probe)
                else:
                    population[i].randomize(begin_index)
                    population[i].combine_oligs(probe, length)
                    population[i].calc_fitness_score(oligo_nodes, probe)
                    mutation_counter += 1
        for i in range(population_size):
            prevent_ineffective_mutation = i in indexes_of_best_list if indexes_of_best_list != len(indexes_of_best_list) - 1 else False
            if not prevent_ineffective_mutation:
                for j in range(best_population_size):
                    if population[i].fit > best_fitness_list[j]:
                        for k in range(best_population_size - 2, j - 1, -1):
                            best_fitness_list[k + 1] = best_fitness_list[k]
                            indexes_of_best_list[k + 1] = indexes_of_best_list[k]
                        best_fitness_list[j] = population[i].fit
                        indexes_of_best_list[j] = i
                        break
        for i in range(iterations - 2, -1, -1):
            best_in_last_generations[i + 1] = best_in_last_generations[i]
        best_in_last_generations[0] = best_fitness_list[0]
        if len(population[indexes_of_best_list[0]]) >= length:
            print(population[indexes_of_best_list[0]].result)
            
            return (population[indexes_of_best_list[0]].fit, population[indexes_of_best_list[0]].result)
    print(population[indexes_of_best_list[0]].result)

    return (population[indexes_of_best_list[0]].fit, population[indexes_of_best_list[0]].result)

if __name__ == "__main__":
    random.seed(time.time())
    if len(sys.argv) < 2:
        print("Podaj nazwe programu, a potem nazwe pliku testowego")
        sys.exit()
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()

    length = int(root.attrib['length'])
    start = root.attrib['start']
    probe = len(start)
    begin_index = 0

    total_nodes = 0
    oligo_nodes = []

    for i, cell in enumerate(root.iter('cell')):
        intensity = int(cell.get('intensity'))
        oligonucleotide = cell.text.strip()
        
        node = OligoNode('',0,0)
        node.index = i
        node.olig = oligonucleotide
        node.matches = convert_intensity(intensity)
        total_nodes += node.matches
        oligo_nodes.append(node)
        
        if start == oligonucleotide:
            begin_index = i
    
    best_population_percentage = 20
    iterations = 100
    mutation_chance = 2
    fit, result_seq = main_algorithm(begin_index, probe, length, best_population_percentage, iterations, mutation_chance)