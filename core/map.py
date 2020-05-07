from scipy.spatial import distance

"""

#/0 = BLOCKED
 /1 = CLEAR
S/2 = START
G/3 = GOAL
$/4 = PASSED

"""
class Map:

    def __init__(self, map_text=None):
        self.map = None
        self.start = None
        self.goal = None
        self.pos = None
        self.points_pos = []
        self.points = 0
        self.cost_till_here = 0

        self.hashed = None

        if map_text!=None:
            self.validateMap(map_text)



    def __lt__(self, other):
        return self.cost_till_here < other.cost_till_here


    def validateMap(self, m):
        m = m.split("\n")

        for i in range(1,len(m),1):
            if len(m[i])!=len(m[0]):
                raise Exception("Map lines have different sizes.")

        i = 0
        j = 0

        self.map = []
        for line in m:
            j=0
            self.map.append([])
            for c in line:
                if ((i==0 or i==len(m)-1) and c!="#") or ((j==0 or j==len(m[i])-1) and c!="#"):
                    raise Exception("Maze borders must be '#'.")
                if c == "#":
                    self.map[i].append(0)
                elif c == " ":
                    self.map[i].append(1)
                elif c.upper() == "S":
                    if self.start!=None:
                        raise Exception("Only one Start is allowed.")
                    self.map[i].append(2)
                    self.start = [j,i]
                    self.pos = [j,i]
                elif c.upper() == "G":
                    if self.goal!=None:
                        raise Exception("Only one Goal is allowed.")
                    self.map[i].append(3)
                    self.goal = [j,i]
                elif c.upper() == "P":
                    self.map[i].append(1)
                    self.points_pos.append([j,i])
                else:
                    raise Exception("Invalid map char: "+c)

                j += 1
            i += 1

        if self.start==None or self.goal==None:
            raise Exception("Start and Goal must be provided")

    def printVisual(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                c = None
                if self.map[i][j]==0:
                    c = "#"
                elif self.map[i][j]==1:
                    c = " "
                elif self.map[i][j]==2:
                    c = "S"
                elif self.map[i][j]==3:
                    c = "G"
                elif self.map[i][j]==4:
                    c = "$"

                for p in self.getPointsLeft():
                    if j==p[0] and i==p[1]:
                        c = "P"

                if i==self.pos[1] and j==self.pos[0]:
                    if self.pos!=self.start:
                        c = "X"
                print(c,end="")
            print("")

    def print(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j],end="")
            print("")

        print(self.points_pos)

    def getPoints(self):
        return self.points

    def getPointsLeft(self):
        return self.points_pos


    def getActions(self):
        ret1 = []
        ret2 = []

        #talvez validar y>0, y<len(self.map)
        #talvez validar x>0, x<len(self.map[0])
        #como as bordas foram validades talvez nao precise

        val = self.map[self.pos[1]][self.pos[0]-1]
        if val!=0 and val!=4:
            ret1.append("E")
            ret2.append(1)

        val = self.map[self.pos[1]][self.pos[0]+1]
        if val!=0 and val!=4:
            ret1.append("D")
            ret2.append(2)

        val = self.map[self.pos[1]+1][self.pos[0]]
        if val!=0 and val!=4:
            ret1.append("B")
            ret2.append(3)


        val = self.map[self.pos[1]-1][self.pos[0]]
        if val!=0 and val!=4:
            ret1.append("C")
            ret2.append(4)

        return ret1, ret2

    def collectPoint(self, i, j):
        # if (i==11 or j==11) and (i==1 or j==1):
            # print(i,j, self.points_pos, "#",[a for a in self.points_pos if not(a[0]==j and a[1]==i)])
            # self.printVisual()
            # sys

        ini = len(self.points_pos)
        self.points_pos = [a for a in self.points_pos if not(a[0]==j and a[1]==i)]
        if len(self.points_pos)!=ini:
            self.points += 1
        # print(i,j, self.points_pos, [a for a in self.points_pos if not(a[0]==j and a[1]==i)])
        # sys.exit()


    def act(self, action):

        if self.solved():
            print("Maze already completed.")
            return False

        if action==1 or action=="E": #moving left
            val = self.map[self.pos[1]][self.pos[0]-1]
            if val==0 or val==4: #check if is blocked or already passed
                return False
            self.map[self.pos[1]][self.pos[0]] = 4 # mark as passed
            self.pos = [self.pos[0]-1,self.pos[1]] # update position
            self.collectPoint(self.pos[1],self.pos[0])
            return True
        elif action==2 or action=="D": #moving right
            val = self.map[self.pos[1]][self.pos[0]+1]
            if val==0 or val==4:
                return False
            self.map[self.pos[1]][self.pos[0]] = 4
            self.pos = [self.pos[0]+1,self.pos[1]]
            self.collectPoint(self.pos[1],self.pos[0])
            return True
        elif action==3 or action=="B": #moving down
            val = self.map[self.pos[1]+1][self.pos[0]]
            if val==0 or val==4:
                return False
            self.map[self.pos[1]][self.pos[0]] = 4
            self.pos = [self.pos[0],self.pos[1]+1]
            self.collectPoint(self.pos[1],self.pos[0])
            return True
        elif action==4 or action=="C": #moving up
            val = self.map[self.pos[1]-1][self.pos[0]]
            if val==0 or val==4:
                return False
            self.map[self.pos[1]][self.pos[0]] = 4
            self.pos = [self.pos[0],self.pos[1]-1]
            self.collectPoint(self.pos[1],self.pos[0])
            return True

        raise Exception("Action unknown")

    def solved(self):
        return self.pos[0]==self.goal[0] and self.pos[1]==self.goal[1]

    def copy(self): # return a copy without references
        ret = Map()
        m = []
        for i in range(len(self.map)):
            m.append([])
            for j in range(len(self.map[i])):
                m[i].append(self.map[i][j])
        ret.map = m
        ret.start = [self.start[0],self.start[1]]
        ret.goal = [self.goal[0],self.goal[1]]
        ret.pos = [self.pos[0],self.pos[1]]
        ret.points = self.points
        ret.points_pos = []
        for p in self.points_pos:
            ret.points_pos.append([p[0],p[1]])

        return ret

    def sim(self, action): # return a Mapa object with the action applied
        ret = self.copy()
        ret.act(action)

        ret.cost_till_here = self.cost_till_here+1
        ret.hashed = None

        return ret

    def getDistance(self):
        v = distance.euclidean(self.pos, self.goal)
        return v

    # def getDistancePoints(self):
    #     points = self.getPointsLeft()
    #     #print(points)
    #     if(len(points)==0):
    #         v = distance.euclidean(self.pos, self.goal)
    #     else:
    #         suma = 0
    #         for ip in points:
    #             v = distance.euclidean(self.pos, ip)
    #             suma = suma + v 
    #         v = suma
    #     return v

    def getDistancePoints(self):
        points = self.getPointsLeft()
        # print(points)
        dis_Pos_Goal = distance.euclidean(self.pos, self.goal)
        dis_Pos_Point = distance.euclidean(self.pos, self.goal)
        dis_Point_Goal = 0
        valeu = 0
        x = 0.0
       
        if(len(points)==0):
            valeu =  dis_Pos_Goal
        else:
            for ip in points:
                if distance.euclidean(self.pos, ip) < dis_Pos_Point:
                    dis_Pos_Point = distance.euclidean(self.pos, ip)
                    dis_Point_Goal = distance.euclidean(ip, self.goal)
        
            v = 0.5*dis_Pos_Point + dis_Point_Goal
            if dis_Pos_Point == 1:
                v=0
            if(v>0):
                x = dis_Pos_Goal/v
            else:
                x = 1
                
            valeu = dis_Pos_Goal + dis_Pos_Goal*(1-x)
        return valeu


    def calculateHash(self):
        self.hashed = "1"
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.hashed += str(self.map[i][j])
        self.hashed = int(self.hashed)

    def __hash__(self):
        if self.hashed==None:
            self.calculateHash()
        return self.hashed