from core.work import Problem, Node
import random

map_dictionnary = { "map1": 2, "map2": 3, "map3": 2, "map4": 2, "map5": 1, "map6": 4,"map7": 26, "map8": 9, "map9": 3, "map10": 2, "map11": 2, "map12": 1, "map13": 3, "map14": 2, "map15": 1}

def return_k_value_for(map_name):
  if map_name in map_dictionnary: 
    return map_dictionnary[map_name]
  return 1

def local_beam_search(problem, k_width):
    """
    From the initial node, Select randomly k states,
    From all the successors, select the k neighbors with highest value,
    Stopping when goal is found or no more successor
    Else repeat process
    """
    current = Node(problem.initial)

    if k_width >= len(current.expand(problem)):
      k_successors = current.expand(problem)
    else:
      k_successors = random.sample(current.expand(problem), k=k_width)

    #check if there are successors to the k successors selected
    if not k_successors:
        return None
    
    explored = set()
    goal_found = False

    while goal_found == False:  
      all_successors = []

      #Generate the successors of all the k best states
      for successor in k_successors:
        children = successor.expand(problem)
        for child in children:
          if child.state not in explored and child not in all_successors:
            all_successors.append(child)
      
      #if there is no successor, we stop
      if not all_successors:
        print("No solution found with width =", k_width)
        break
      
      #check if any successor is a goal
      for successor in all_successors:
        if problem.goal_test(successor.state):
          goal_found = True
          print("Solution found for width =", k_width)
          return successor
      
      #Select the k best successors
      all_successors.sort(key=lambda node: node.state.getPoints(), reverse=False)
      k_successors = all_successors[:k_width]
      
      #Mark the k successors as explored, to avoid exploring same nodes
      for successor in k_successors:
        explored.add(successor.state)

    return None
      
def k_states_local_beam_search(problem, map_name=None):
  k = 1
  if map_name:
    k = return_k_value_for(map_name)
  k_max = 100
  result = None
  while result == None:
    result = local_beam_search(problem, k)
    k = k + 1
    if k > k_max:
      break
  
  return result
   
