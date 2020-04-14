from core.work import Problem, Node


def DepthFirst(problem):

    frontier = [Node(problem.initial)]

    while frontier:

        node = frontier.pop()

        if problem.goal_test(node.state):
            return node

        frontier.extend(node.expand(problem))

    return None
