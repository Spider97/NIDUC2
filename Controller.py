import random

class Controller:
    def __init__(self, frame_size, frames, myList):
        self.frame_size=frame_size
        self.frames=frames
        if myList is None:
            myList=[]
        self.myList = myList
        self.signal=0
    def generate(self):
        x=''
        y=''
        for i in range(self.frames):
            tab=[]
            for j in range(self.frame_size):
                y=str(random.randint(0, 1))
                x=y+x
            self.myList.append(x)
            x=''

    def display(self):
        for i in range(self.frames):
            print(self.myList[i])


    def addParity(self):
        one=0
        for j in range(self.frames):
            x = self.myList[j]
            for i in range(self.frame_size):
                if (x[i] == '1'):
                    one = one+1
                if (one%2==0):
                    self.myList[j]=x+'0'
                if (one%2!=0):
                    self.myList[j]=x+'1'
            one=0
        self.frame_size=self.frame_size+1

    def BSC(self):
        z=''
        number=random.randint(0, self.frames-1)
        position=random.randint(0, len(self.myList[0])-1)
        s=list(self.myList[number])
        actual=self.myList[number]
        if (actual[position] =='0'):
            s[position]= '1'
            s.reverse()
            for j in range(self.frame_size):
                y=s[j]
                z=y+z
        if (actual[position] == '1'):
            s[position]= '0'
            s.reverse()
            for k in range(self.frame_size):
                y=s[k]
                z=y+z
        self.myList[number]=z

    def saw(self):
        for i in range(self.frames):
            while(self.signal!=1):
                print(self.myList[i])
                self.setSignal()
                if(self.signal==0):
                    print("Powtorne przesylanie danych")
            self.signal=0

    def setSignal(self):
            my_input = int(input("Czy dane zostaly dostarczone 0-nie/1-tak: "))
            self.signal=my_input
            print()




