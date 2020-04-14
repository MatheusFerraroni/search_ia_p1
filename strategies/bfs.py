from collections import deque
import sys
sys.path.insert(1, '../core/')
import Trabalho


def bfs(problem):
    frontier = deque([Trabalho.NodeTrab(problem.initial)])
    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None