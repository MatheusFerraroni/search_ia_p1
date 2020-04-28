import sys

from core.work import Problem, Node
from utils import *


def Greedy(problem):

    frontier = [Node(problem.initial)]

    while frontier:

        node = frontier.pop()

        if problem.goal_test(node.state):
            return node

        frontier.extend(node.expand(problem))

    return None
