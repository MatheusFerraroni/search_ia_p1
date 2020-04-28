from collections import deque
import sys

from core.work import Problem, Node


def BreadthFirst(problem):

    frontier = deque([Node(problem.initial)])

    while frontier:

        node = frontier.popleft()

        if problem.goal_test(node.state):
            return node

        frontier.extend(node.expand(problem))

    return None


    