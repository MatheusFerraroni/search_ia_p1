import sys
import time
sys.path.insert(1, './core/')
import Mapa
import Trabalho
sys.path.insert(1, './strategies/')
from bfs import *


def main(map_text):

    print("""\nLegenda do mapa:
#/0 = BLOCKED
 /1 = CLEAR
S/2 = START
G/3 = GOAL
$/4 = PASSED\n\n""")

    print("""Legenda de acoes:
1/E = LEFT
2/D = RIGHT
3/B = DOWN
4/C = UP\n\n""")

    print("Criando mapa")
    initial_state = Mapa.Mapa(map_text)
    print("Criando mapa OK.")

    print("Criando problema")
    problema = Trabalho.ProblemTrab(initial_state)
    print("Criando problema OK")


    print("Executando BFS")
    ini = time.time()
    res = bfs(problema)
    tempo = time.time()-ini
    print("Executando BFS OK. Tempo gasto: ", str(tempo), " Segundos")


    print("Acoes tomadas: ", res.solution())


    print("START")
    initial_state.printVisual()
    for act in res.solution():
        print("ACTION: ",act)
        initial_state.act(act)
        initial_state.printVisual()


if __name__ == '__main__':
    try:
        map_file = sys.argv[1]
        f = open(map_file,"r")
        map_file = f.read()
        f.close()
    except Exception as e:
        print("Error loading the map file: "+str(e))
        sys.exit()


    main(map_file)