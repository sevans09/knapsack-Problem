import random, operator
import numpy as np
import math
class box:
  def __init__(self, v, w, gen):
    self.p = v # Item's priority
    self.w = w #Item's weight
    self.gen = gen
    self.bests = []


# Change POP_SIZE and MAX_GENERATIONS to test further
POP_SIZE = 50
CULL_AMOUNT = 0.5
MAX_CAPACITY = 120
MAX_GENERATIONS = 20
NUM_ITEMS = 7
MUTATION_CHANCE = 0.4
MAX_PRIO = 0
TEMP_BEST_BACKPACK = [0,0,0,0,0,0,0]

""" 
fitness function
input:   target is the population  
output:  total_priority
purpose: will return the fitness value of permutation named "target".
           Higher scores are better and are equal to the total value of items in the permutation.
""" 
def fitness(target, ITEMS, max_prio):
    total_priority = 0
    total_weight = 0
    index = 0

    global MAX_PRIO
    global TEMP_BEST_BACKPACK
    popArray = np.asarray(target)
    nRows = math.ceil(len(popArray)/7)
    popArray = popArray.reshape(nRows,7)
  
    for i in range(nRows):
      if total_priority > MAX_PRIO and total_weight < MAX_CAPACITY:
        MAX_PRIO = total_priority
        print("New best config: ", popArray[i-1])
        print("Priority found", MAX_PRIO)
        TEMP_BEST_BACKPACK = popArray[i-1] 

      total_weight = 0
      total_priority = 0

      # Add up each array of 7 to find best configuration
      for j in range(0,7):
          total_priority += popArray[i][j] * ITEMS[j].p
          total_weight += popArray[i][j] * ITEMS[j].w

    return MAX_PRIO
        

"""
spawn initial population
output: set of randomly generated values
purpose: generate a random starting population of random individuals
"""
def spawn_population():
  # Generate random genes for the starting population
  population = []
  for i in range (0, POP_SIZE):
    # Generate a random gene
    for i in range(0, NUM_ITEMS):
      rand = random.randint(0,1)
      population.append(rand)
  return population

"""
mutate function
input:   Parent from evolve function
output:  The parent after cross over
pupose:  Cross over based on random chance 
"""
def mutate(parents):
  index = 0
  for r in enumerate(parents):
    if index >= len(parents):
      break
    if random.random() > MUTATION_CHANCE:
        continue
    else:
      if parents[index] == 0:
        parents[index] = 1
      else:
        parents[index] = 0
    index = index + 1
  return parents

"""
evolve population
input: population
output: return parent after mutation
purpose: cull the population, cross it over by calling mutate
         
"""
def evolve_population(pop):
  parent_eligibility = 0.2
  mutation_chance = 0.08
  parent_lottery = 0.05
  remainder = (len(pop)/2) % 7 
  pop = pop[:math.floor(len(pop)/2 - remainder + 1)]
  parent_length = math.floor(len(pop)/2)
  parents = pop[:parent_length]
  nonparents = pop[parent_length+1:]

  # first cut the population 
  # combine the first half of first chile with second half of second child (2 children)
  for np in nonparents:
         parents.append(np)

  # After crossing over, mutate to ensure global 
  # optima are reached
  parents = mutate(parents)
  return parents


def main():
  # define the boxes each box has a priority, weight and generation. Gen is set to 1 for the initialization.
  box1 = box(6,20,1)
  box2 = box(5,30,1)
  box3 = box(8,60,1)
  box4 = box(7, 90,1)
  box5 = box(6,50,1)
  box6 = box(9,70,1)
  box7 = box(4,30,1)
  # A list of all boxes
  ITEMS = [box1,box2,box3,box4,box5,box6,box7]

  # pop is our initial population 
  pop = spawn_population()
  
  gen_number = 0
  for gen in range(0, MAX_GENERATIONS):
    for i in range(len(pop)):
      gen_number = gen_number + 1
      if len(pop) == 0:
        break
      print("Generation: ", gen_number)
      print("Population size: ", len(pop))
      pop = sorted(pop, key=lambda item: fitness(pop, ITEMS, MAX_PRIO), reverse=True)
      pop = evolve_population(pop)
  

  print("Max priority found that is contained within constraints:", fitness(pop, ITEMS, MAX_PRIO))
  print("Best backpack configuration: ", TEMP_BEST_BACKPACK)
  return True


if __name__ == "__main__":
  main()
