import random
from box import box

POP_SIZE = 5
CULL_AMOUNT = 0.5
MAX_CAPACITY = 120
MAX_GENERATIONS = 20
NUM_ITEMS = 7

box1 = box(6,20)
box2 = box(5,30)
box3 = box(8,60)
box4 = (7, 90)
box5 = (6,50)
box6 = (9,70)
box7 = (4,30)
ITEMS = [box1,box2,box3,box4,box5,box6,box7]


""" 
fitness function
input:   target 
output:  total_value
purpose: will return the fitness value of permutation named "target".
           Higher scores are better and are equal to the total value of items in the permutation.
""" 
def fitness(target):
    total_priority = 0
    total_weight = 0
    index = 0
    print("in fitenees function")
    print("target is ", target)
    for i in target:
        print("in fitenees function, i is", i)
        if index >= len(ITEMS):
            break
        if (i == 1):
            total_priority += ITEMS[index].p
            total_weight += ITEMS[index].w
        index += 1
    
    if total_weight > MAX_CAPACITY:
        # Not valid!
        return 0
    else:
        # OK to consider
        return total_priority

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
pupose: checks whether the box is in the gene or not
"""
def mutate(target):
    if target[r] > 0:
        target[r] = 0
    else:
        target[r] = target.p * target.w
        

"""
evolve population
"""
def evolve_population(pop):
  parent_eligibility = 0.2
  mutation_chance = 0.08
  parent_lottery = 0.05
  parent_length = int(parent_eligibility*len(pop))
  parents = pop[:parent_length]
  nonparents = pop[parent_length:]
  for np in nonparents:
    if parent_lottery > random.random():
         parents.append(np)
  
  return parents

def breed_children(parents):
  pass

def main():
  generation = 0
  pop = spawn_population()

  for gen in range(0, MAX_GENERATIONS):
    generation = generation + 1
    for item in ITEMS:
      print("Generation: ", generation)
      print("Population size: ", len(pop))
      print("item is ", item)
      print("fitness is ", fitness(item))
      pop = sorted(pop, key=lambda item: fitness(item), reverse=True)

      pop = evolve_population(pop)

  return True


if __name__ == "__main__":
  main()
