import random

class pointmap:
    def __init__(self,type,hp = 255):
        self.type = type
        self.hp = hp

class map:
    def __init__(self,w,h):
        self.wpoint = w
        self.hpoint = h
        self.w = w * 2 + 1
        self.h = h * 2 + 1
        self.maplab = [[0 for q in range(self.h)] for i in range(self.w)]
        for x in range(self.w):
            for y in range(self.h):
                if (x + 1) % 2 != 0 or (y + 1) % 2 != 0:
                    self.maplab[x][y] = 1
        self.listpoint = [[q // h, q % h] for q in range(w * h)]
        self.pointb = []
        while len(self.listpoint) > 0:
            if len(self.pointb) == 0:
                pint = random.randint(0,len(self.listpoint) - 1)
                point = self.listpoint[pint]
                del self.listpoint[pint]
                self.pointb += [[point[0],point[1]]]
            else:
                point = random.choice(self.pointb)
            while True:
                i = random.randint(0, 3)
                if self.pointif([point[0],point[1]], i) == True:
                    if i == 0:
                        self.maplab[(point[0]) * 2 + 1][(point[1]) * 2 + 1 - 1] = 0
                        point[1] -= 1
                    if i == 1:
                        self.maplab[(point[0]) * 2 + 1 + 1][(point[1]) * 2 + 1] = 0
                        point[0] += 1
                    if i == 2:
                        self.maplab[(point[0]) * 2 + 1][(point[1]) * 2 + 1 + 1] = 0
                        point[1] += 1
                    if i == 3:
                        self.maplab[(point[0]) * 2 + 1 - 1][(point[1]) * 2 + 1] = 0
                        point[0] -= 1
                    self.pointb += [[point[0],point[1]]]
                    for q in range(len(self.listpoint)):
                        if self.listpoint[q] == point:
                            del self.listpoint[q]
                            break
                else:
                    break

        self.listexid = []
        for q in range(w):
            self.listexid.append([q * 2 + 1, 0])
            self.listexid.append([q * 2 + 1, (h) * 2 ])
        for q in range(h):
            self.listexid.append([0,q * 2 + 1])
            self.listexid.append([(w) * 2,q * 2 + 1])

        print(self.listexid)

        point = random.choice(self.listexid)
        del self.listexid[self.listexid.index(point)]
        self.maplab[point[0]][point[1]] = 2

        self.zeropoint = []

        for q in range(len(self.maplab)):
            for i in range(len(self.maplab[q])):
                if self.maplab[q][i] == 0:
                    self.zeropoint.append([q,i])

        for q in range(len(self.maplab)):
            for i in range(len(self.maplab[q])):
                self.maplab[q][i] = pointmap(self.maplab[q][i])

        for q in range(3):
            point = random.choice(self.zeropoint)
            self.maplab[point[0]][point[1]] = pointmap(3,hp=random.randint(10,100))

        point = random.choice(self.zeropoint)
        self.maplab[point[0]][point[1]] = pointmap(4)




    def print(self):
        a = {1:'##', 0:'  ',2:'00',3:'vr',4:'up'}
        for q in range(self.w):
            s = ''
            for i in range(self.h):
                s += a[self.maplab[q][i].type]
            print(s)

    def pointif(self,point,i):
        if i == 0:
            point[1] -= 1
        elif i == 1:
            point[0] += 1
        elif i == 2:
            point[1] += 1
        elif i == 3:
            point[0] -= 1
        flag = False
        if self.listpoint.count(point) > 0:
            flag = True
        return flag

class hero:
    def __init__(self,map):
        self.lvl = 1
        self.hp = 255
        self.map = map
        self.point = random.choice(self.map.zeropoint)
        self.vektor = 0
        self.win = False
        self.seep()

    def print(self):
        print("{} {} {} {}".format(self.map.maplab[self.seepoint[0]][self.seepoint[1]].type,
            self.map.maplab[self.seepoint[0]][self.seepoint[1]].hp,self.lvl,self.hp))
        print(self.point)
        print(self.vektor)

    def seep(self):
        point = [self.point[0], self.point[1]]
        if self.vektor == 0:
            point[1] -= 1
        if self.vektor == 1:
            point[0] += 1
        if self.vektor == 2:
            point[1] += 1
        if self.vektor == 3:
            point[0] -= 1
        self.seepoint = point

    def command(self,com):
        if com == 0:
            if self.map.maplab[self.seepoint[0]][self.seepoint[1]].type == 0:
                self.point = [self.seepoint[0], self.seepoint[1]]
                self.seep()
            elif self.map.maplab[self.seepoint[0]][self.seepoint[1]].type == 2:
                print("you win")
                self.win = True 
            elif self.map.maplab[self.seepoint[0]][self.seepoint[1]].type == 3:
                self.hp -= self.map.maplab[self.seepoint[0]][self.seepoint[1]].hp / self.lvl 
                self.map.maplab[self.seepoint[0]][self.seepoint[1]] = pointmap(0)
                if self.hp <= 0:
                    print('you lose')
                    self.win = True
                self.point = [self.seepoint[0], self.seepoint[1]]
                self.seep()
            elif self.map.maplab[self.seepoint[0]][self.seepoint[1]].type == 4:
                self.map.maplab[self.seepoint[0]][self.seepoint[1]] = pointmap(0)
                self.lvl += 1
                self.point = [self.seepoint[0], self.seepoint[1]]
                self.seep()
        elif com == 1:
            self.vektor = (self.vektor + 1) % 4
            self.seep()





M = map(20,20)
M.print()
hero = hero(M)

while not hero.win:
    hero.print()
    hero.command(int(input()))