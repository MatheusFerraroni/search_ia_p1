import sys

from core.work import Problem, Node
sys.path.insert(1, '../aima-python/')
from utils import *


def recursive_best_first_search(problem, h=None):
    """[Figure 3.26] Recursive best-first search (RBFS) is an
    informative search algorithm. Like A*, it uses the heuristic
    f(n) = g(n) + h(n) to determine the next node to expand, making
    it both optimal and complete (iff the heuristic is consistent).
    To reduce memory consumption, RBFS uses a depth first search
    and only retains the best f values of its ancestors."""
    h = memoize(h or problem.h, 'h')

    infinity = 999999999


    def RBFS(problem, node, flimit):
        if problem.goal_test(node.state):
            return node, 0   # (The second value is immaterial)
        successors = node.expand(problem)
        if len(successors) == 0:
            return None, infinity
        for s in successors:
            s.f = max(s.path_cost + h(s), node.f)
        while True:
            # Order by lowest f value
            successors.sort(key=lambda x: x.f)
            best = successors[0]
            if best.f > flimit:
                return None, best.f
            if len(successors) > 1:
                alternative = successors[1].f
            else:
                alternative = infinity
            result, best.f = RBFS(problem, best, min(flimit, alternative))
            if result is not None:
                return result, best.f

    node = Node(problem.initial)
    node.f = h(node)
    result, bestf = RBFS(problem, node, infinity)
    return result