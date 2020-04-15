import sys
import time
import argparse

from core.map import Map
from core.work import Problem, Node
from strategies.bfs import BreadthFirst
from strategies.dfs import DepthFirst


def read_maps(args):

    maps = []

    for map_file in args.maps:

        try:
            f = open(map_file,"r")
            maps.append(f.read())
            f.close()
        except Exception as e:
            print("Error loading the map file: " + str(e))
            pass

    if not maps:
        sys.exit()

    return maps


def execute(strategy, map_text, args):

    print("""Action Legend:
            1/E = LEFT
            2/D = RIGHT
            3/B = DOWN
            4/C = UP\n\n""")

    print("Criando mapa")
    initial_state = Map(map_text)
    print("Criando mapa OK.")

    print("Criando problema")
    problem = Problem(initial_state)
    print("Criando problema OK")

    print("Executando {0}".format(strategy.__name__))
    ini = time.time()
    res = strategy(problem)
    tempo = time.time()-ini
    print("Executando {0} OK".format(strategy.__name__))
    print("Time: {0}".format(str(tempo)))
    print("Node: {0}".format(str(problem.total_nodes)))
    print("Actions: ", res.solution())

    if args.print:
        print("""\nMap Legend:
                #/0 = BLOCKED
                 /1 = CLEAR
                S/2 = START
                G/3 = GOAL
                $/4 = PASSED\n\n""")

        print("START")
        initial_state.printVisual()
        for act in res.solution():
            print("ACTION: ",act)
            initial_state.act(act)
            initial_state.printVisual()

    print('--------------------------------------------\n\n')


def main(args):

    maps = read_maps(args)

    for map in maps:

        for i in range(args.times[0]):

            ####################################
            # ADD STRATEGY CALL HERE
            ####################################
            if args.bfs:
                execute(BreadthFirst, map, args)

            if args.dfs:
                execute(DepthFirst, map, args)

            if args.all:
                for strategy in [BreadthFirst, DepthFirst]:
                    execute(strategy, map, args)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Execution parameters')
    parser.add_argument('--times', metavar='t', type=int, nargs=1, default=[1], action='store', help='Quantity of times executed')
    parser.add_argument('--maps', metavar='c', type=str, nargs='*', default=['./maps/map1.txt'], action='store', help='File path')

    ####################################
    # ADD STRATEGY FLAG HERE
    ####################################
    parser.add_argument('--bfs', help='Breadth-first search', action='store_true')
    parser.add_argument('--dfs', help='Depth-first search', action='store_true')
    parser.add_argument('--all', help='All search strategies', action='store_true')

    parser.add_argument('--print', help='Put it if want to print result', action='store_true')

    args = parser.parse_args()

    main(args)