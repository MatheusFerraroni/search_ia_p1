from core.work import Problem, Node
import random

k_width = 3

def k_states_local_beam_search(problem):
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
    explored_positions = []
    goal_found = False

    explored_positions.append(current.state.pos)
    for successor in k_successors:
      explored_positions.append(successor.state.pos)

    while goal_found == False:  
      all_successors = []
      possible_positions = []

      #Generate the successors of all the k best states
      for successor in k_successors:
        children = successor.expand(problem)
        for child in children:
          if child.state not in explored and child.state.pos not in possible_positions and child.state.pos not in explored_positions and child not in all_successors:
            all_successors.append(child)
            possible_positions.append(child.state.pos)
      
      #if there is no successor, we stop
      if not all_successors:
        break
      
      #check if any successor is a goal
      for successor in all_successors:
        if problem.goal_test(successor.state):
          goal_found = True
          return successor
      
      #Select the k best successors
      all_successors.sort(key=lambda node: node.state.getPoints(), reverse=False)
      k_successors = all_successors[:k_width]
      
      #Mark the k successors as explored, to avoid exploring same nodes
      for successor in k_successors:
        explored.add(successor.state)
        explored_positions.append(successor.state.pos)

    return None
      
   
