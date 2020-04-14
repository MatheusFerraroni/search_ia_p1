

"""

#/0 = BLOCKED
 /1 = CLEAR
S/2 = START
G/3 = GOAL
$/4 = PASSED

"""
class Mapa:
    def __init__(self, map_text=None):
        self.mapa = None
        self.start = None
        self.goal = None
        self.pos = None

        if map_text!=None:
            self.validateMap(map_text)


    def validateMap(self, m):
        m = m.split("\n")

        for i in range(1,len(m),1):
            if len(m[i])!=len(m[0]):
                raise Exception("Map lines have different sizes.")

        i = 0
        j = 0

        self.mapa = []
        for line in m:
            j=0
            self.mapa.append([])
            for c in line:
                if ((i==0 or i==len(m)-1) and c!="#") or ((j==0 or j==len(m[i])-1) and c!="#"):
                    raise Exception("Maze borders must be '#'.")
                if c == "#":
                    self.mapa[i].append(0)
                elif c == " ":
                    self.mapa[i].append(1)
                elif c == "S" or c == "s":
                    if self.start!=None:
                        raise Exception("Only one Start is allowed.")
                    self.mapa[i].append(2)
                    self.start = [j,i]
                    self.pos = [j,i]
                elif c == "G" or c == "g":
                    if self.goal!=None:
                        raise Exception("Only one Goal is allowed.")
                    self.mapa[i].append(3)
                    self.goal = [j,i]
                j += 1
            i += 1

        if self.start==None or self.goal==None:
            raise Exception("Start and Goal must be provided")


    def printVisual(self):
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                c = None
                if self.mapa[i][j]==0:
                    c = "#"
                elif self.mapa[i][j]==1:
                    c = " "
                elif self.mapa[i][j]==2:
                    c = "S"
                elif self.mapa[i][j]==3:
                    c = "G"
                elif self.mapa[i][j]==4:
                    c = "$"

                if i==self.pos[1] and j==self.pos[0]:
                    if self.pos!=self.start:
                        c = "X"
                print(c,end="")
            print("")

    def print(self):
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                print(self.mapa[i][j],end="")
            print("")


    def getActions(self):
        ret1 = []
        ret2 = []

        #talvez validar y>0, y<len(self.map)
        #talvez validar x>0, x<len(self.map[0])
        #como as bordas foram validades talvez nao precise

        val = self.mapa[self.pos[1]][self.pos[0]-1]
        if val!=0 and val!=4:
            ret1.append("E")
            ret2.append(1)

        val = self.mapa[self.pos[1]][self.pos[0]+1]
        if val!=0 and val!=4:
            ret1.append("D")
            ret2.append(2)

        val = self.mapa[self.pos[1]+1][self.pos[0]]
        if val!=0 and val!=4:
            ret1.append("B")
            ret2.append(3)

        val = self.mapa[self.pos[1]-1][self.pos[0]]
        if val!=0 and val!=4:
            ret1.append("C")
            ret2.append(4)

        return ret1, ret2

    def act(self, action):

        if self.solved():
            print("Maze already completed.")
            return False

        if action==1 or action=="E": #moving left
            val = self.mapa[self.pos[1]][self.pos[0]-1]
            if val==0 or val==4: #check if is blocked or already passed
                return False
            self.mapa[self.pos[1]][self.pos[0]] = 4 # mark as passed
            self.pos = [self.pos[0]-1,self.pos[1]] # update position
            return True
        elif action==2 or action=="D": #moving right
            val = self.mapa[self.pos[1]][self.pos[0]+1]
            if val==0 or val==4:
                return False
            self.mapa[self.pos[1]][self.pos[0]] = 4
            self.pos = [self.pos[0]+1,self.pos[1]]
            return True
        elif action==3 or action=="B": #moving down
            val = self.mapa[self.pos[1]+1][self.pos[0]]
            if val==0 or val==4:
                return False
            self.mapa[self.pos[1]][self.pos[0]] = 4
            self.pos = [self.pos[0],self.pos[1]+1]
            return True
        elif action==4 or action=="C": #moving up
            val = self.mapa[self.pos[1]-1][self.pos[0]]
            if val==0 or val==4:
                return False
            self.mapa[self.pos[1]][self.pos[0]] = 4
            self.pos = [self.pos[0],self.pos[1]-1]
            return True

        raise Exception("Action unknown")

    def solved(self):
        return self.pos[0]==self.goal[0] and self.pos[1]==self.goal[1]

    def copy(self): # return a copy without references
        ret = Mapa()
        m = []
        for i in range(len(self.mapa)):
            m.append([])
            for j in range(len(self.mapa[i])):
                m[i].append(self.mapa[i][j])
        ret.mapa = m
        ret.start = [self.start[0],self.start[1]]
        ret.goal = [self.goal[0],self.goal[1]]
        ret.pos = [self.pos[0],self.pos[1]]

        return ret

    def sim(self, action): # return a Mapa object with the action applied
        ret = self.copy()
        ret.act(action)
        return ret