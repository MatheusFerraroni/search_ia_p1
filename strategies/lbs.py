def k_states_local_beam_search(problem, k):
    """
    From the initial node, Select randomly k states,
    From all the successors, select the k neighbors with highest value,
    Stopping when goal is found or no more successor
    Else repeat process
    """
    current = Node(problem.initial)
    k_successors = random.choices(current.expand(problem), k=k)
    #check if there are successors to the k successors selected
    if not k_successors:
        break
    explored = set()
    
    while True:
        all_successors = []
        #Generate the successors of all the k best states
        for successor in k_successors:
          children = successor.expand(problem)
          for child in children:
            if child not in explored and child not in all_successors:
              all_successors.add(child)
        #if there is no successor, we stop
        if not all_successors:
            break
        #check if any successor is a goal
        for successor in all_successors:
          if problem.goal_test(successor.state):
              break
        #Select the k best successors
        all_successors.sort(key=lambda node: problem.value(node.state), reverse=True)
        k_successors = all_successors[:k]
        #Mark the k successors as explored, to avoid exploring same nodes
        for successor in k_successors:
          explored.add(successor.state)
    
    return explored
