#README
#This Library/Utility has been developed by Pooria Ahmadi and feel free to edit it and use it easily :), If you want, you can send me the edited version and let me add the edited ones to base library and mention you in the main file.
#!!! Please don't sell this Utility !!!
#Discord: https://discord.gg/F6MV4Pu5mu
#Github: https://github.com/pooriaahmadi
#Youtube: https://www.youtube.com/channel/UCJd8Q9A-fyIpajhLvCvjViA
#Documnetions are in guthub and toturials are in YT channel
#imports
import os
import turtle as tr
import datetime as dt
import random
#global variables
date=dt.datetime.now()
#classes
class _file:
    def createFile(destination, data=""):
        destination = open(destination, "wt")
        destination.write(data)
        destination.close()
    def copy(source, destination=""):
        source = open(source, "rb")
        destination = open(destination, "wb")
        destination.write(source.read())
        source.close()
        destination.close()
    def delete(target):
        os.remove(target)
    def read(target):
        target = open(target, "rb")
        result = target.read()
        target.close()
        return result
    def writeFile(target, data):
        target = open(target, "wt")
        target.write(data)
        target.close()
    def appenFile(target, data):
        target = open(target, "at")
        target.write(data)
        target.close()
class _turtle:
    def __init__(self):
        self.pen = tr.Turtle()
    @property
    def pen(self):
        return self.__pen
    @pen.setter
    def pen(self, pen):
        self.__pen = pen
    def createShape(self, sides=3, sideLength=100, isRandom=False):
        if isRandom:
            for i in range(sides):
                self.setColor(isRandom=True)
                self.forward(sideLength)
                self.left(360/sides)
        else:
            for i in range(sides):
                self.forward(sideLength)
                self.left(360/sides)
    def createMaze(self, times=500, degree=90, isRandom=False):
        if isRandom:
            for i in range(times):
                self.setColor(isRandom=True)
                self.forward(i)
                self.left(degree)
        else:
            for i in range(times):
                self.forward(i)
                self.left(degree)
    def setSpeed(self, newSpeed=0):
        self.pen.speed(newSpeed)
    def setColor(self, rgb=(0,0,0), isRandom=False):
        if isRandom:
            self.pen.color(random.randrange(255)/255,random.randrange(255)/255,random.randrange(255)/255)
        else:
            self.pen.color(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    def setPos(self, x=0, y=0, isDown=True):
        if isDown:
            self.pen.down()
            self.pen.goto(x,y)
        else:
            self.pen.up()
            self.pen.goto(x,y)
            self.pen.down()
    def forward(self, length=100, isDown=True):
        if isDown:
            self.pen.down()
            self.pen.fd(length)
        else:
            self.pen.up()
            self.pen.fd(length)
            self.pen.down()
    def backward(self, length=100, isDown=True):
        if isDown:
            self.pen.down()
            self.pen.bk(length)
        else:
            self.pen.up()
            self.pen.bk(length)
            self.pen.down()
    def up(self):
        self.pen.up()
    def down(self):
        self.pen.down()
    def left(self, degree=90):
        self.pen.left(degree)
    def right(self, degree=90):
        self.pen.right(degree)
class _math:
    class fraction:
        def __init__(self, f1=1, f2=2):
            self.f1 = f1
            self.f2 = f2
        @property
        def f1(self):
            return self.__f1
        @f1.setter
        def f1(self, f1):
            self.__f1 = f1
        @property
        def f2(self):
            return self.__f2
        @f2.setter
        def f2(self, f2):
            if f2==0:
                self.__f2 = 1
            else:
                self.__f2 = f2
        def __repr__(self):
            if self.f2 == 1:
                return f"{self.f1}"
            return f"{self.f1}/{self.f2}"
        def __abs__(self):
            return self.f1/self.f2
        def __add__(self, secondFraction):
            return _math.fraction(self.f1*secondFraction.f2+self.f2*secondFraction.f1,self.f2*secondFraction.f2)
        def __sub__(self, secondFraction):
            return _math.fraction(self.f1*secondFraction.f2-self.f2*secondFraction.f1,self.f2*secondFraction.f2)
        def __neg__(self):
            return _math.fraction(-self.f1, self.f2)
        def __mul__(self, secondFraction):
            return _math.fraction(self.f1*secondFraction.f1, self.f2*secondFraction.f2)
        def __invert__(self):
            return _math.fraction(self.f2, self.f1)
        def __eq__(self, secondFraction):
            return self.__abs__()==secondFraction.__abs__()
        def __lt__(self, secondFraction):
            return self.__abs__()<secondFraction.__abs__()
        def __le__(self, secondFraction):
            return self.__abs__()<=secondFraction.__abs__()
        def __bt__(self, secondFraction):
            return self.__abs__()>secondFraction.__abs__()
        def __be__(self, secondFraction):
            return self.__abs__()>=secondFraction.__abs__()
class _random:
    class randomNumber:
        def __init__(self, startNumber=0, endNumber=1):
            self.startNumber = startNumber
            self.endNumber = endNumber
        @property
        def startNumber(self):
            return self.__startNumber
        @startNumber.setter
        def startNumber(self, startNumber):
            if startNumber>=0:
                self.__startNumber = startNumber
            else:
                self.__startNumber = 0
        @property
        def endNumber(self):
            return self.__endNumber
        @endNumber.setter
        def endNumber(self, endNumber):
            if endNumber>=0:
                self.__endNumber = endNumber
            else:
                self.__endNumber = self.startNumber+1
        def runApp(self):
            return random.randrange(self.startNumber, self.endNumber)
        def __repr__(self):
            return f"{self.runApp()}"
    class randomCharacter:
        def __init__(self, startChar='A', endChar='z'):
            self.startChar = startChar
            self.endChar = endChar
        @property
        def startChar(self):
            return self.__startChar
        @startChar.setter
        def startChar(self, startChar):
            if isinstance(startChar, int):
                self.__startChar = startChar
            else:
                try:
                    self.__startChar =  ord(startChar)
                except Exception as e:
                    self.__startChar = 0
        @property
        def endChar(self):
            return self.__endChar
        @endChar.setter
        def endChar(self, endChar):
            if isinstance(endChar, int):
                self.__endChar = endChar
            else:
                try:
                    self.__endChar =  ord(endChar)
                except Exception as e:
                    self.__endChar = self.startchar+1
        def runApp(self):
            return chr(random.randrange(self.startChar, self.endChar))
        def __repr__(self):
            return self.runApp()
    class randomCharacters(randomCharacter):
        def __init__(self, length = 5, startChar = 'A', endChar = 'z'):
            super().__init__(startChar, endChar)
            self.length = length
        @property
        def length(self):
            return self.__length
        @length.setter
        def length(self, length):
            if length>0:
                self.__length = length
            else:
                self.__length = 1
        def runApp(self):
            tmp = ''
            for i in range(self.length):
                tmp = tmp + chr(random.randrange(self.startChar, self.endChar))
            return tmp
        def __repr__(self):
            return self.runApp()
    class randomNumbers:
        def __init__(self, length=5):
            self.length = length
        @property
        def length(self):
            return self.__length
        @length.setter
        def length(self, length):
            if length>0:
                self.__length = length
            else:
                self.__length = 5
        def runApp(self):
            tmp = 0
            for i in range(self.length):
                tmp *= 10
                tmp = tmp + random.randrange(0,9)
            return tmp
        def __repr__(self):
            return f"{self.runApp()}"
    class randomNumbersAndCharacters:
        def __init__(self, length=5):
            self.length = length
        @property
        def length(self):
            return self.__length
        @length.setter
        def length(self, length):
            if length>0:
                self.__length = length
            else:
                self.__length = 5
        def runApp(self):
            tmp = ''
            for i in range(self.length):
                if random.randrange(0,2):
                    tmp = tmp+chr(random.randrange(ord('A'),ord('z')))
                else:
                    tmp = tmp+str(random.randrange(10))
            return tmp
        def __repr__(self):
            return self.runApp()
class _time:
    class date:
        def __init__(self, day=date.day, month=date.month, year=date.year):
            self.year = year
            self.month = month
            self.day = day
        @property
        def day(self):
            return self.__day
        @day.setter
        def day(self, day):
            if day>0 and day<31:
                self.__day = day
            else:
                self.__day = 1
                for i in range(day//30):
                    self.month += 1
        @property
        def month(self):
            return self.__month
        @month.setter
        def month(self, month):
            if month<13 and month>0:
                self.__month = month
            else:
                self.__month = 1
                for i in range(month//12):
                    self.year += 1
        @property
        def year(self):
            return self.__year
        @year.setter
        def year(self, year):
            if year>0:
                self.__year = year
            else:
                self.__year = date.year
        def __repr__(self):
            return f"{self.month}/{self.day}/{self.year}"
        def tik(self):
            self.day += 1
    class clock:
        def __init__(self, ms=date.microsecond//100, second=date.second, minute=date.minute, hour=date.hour):
            self.hour = hour
            self.minute = minute
            self.second = second
            self.ms = ms
        @property
        def ms(self):
            return self.__ms
        @ms.setter
        def ms(self, ms):
            if ms<1000 and ms>0:
                self.__ms = ms
            else:
                self.__ms = 1
                for i in range(ms//1000):
                    self.second +=1
        @property
        def second(self):
            return self.__second
        @second.setter
        def second(self, second):
            if second<60 and second>0:
                self.__second = second
            else:
                self.__second = 1
                for i in range(second//60):
                    self.minute += 1
        @property
        def minute(self):
            return self.__minute
        @minute.setter
        def minute(self, minute):
            if minute<60 and minute>0:
                self.__minute = minute
            else:
                self.__minute = 1
                for i in range(minute//60):
                    self.hour += 1
        @property
        def hour(self):
            return self.__hour
        @hour.setter
        def hour(self,hour):
            if hour<24 and hour>0:
                self.__hour = hour
            else:
                self.__hour = 1
        def __repr__(self):
            return f"{self.hour}:{self.minute}:{self.second}:{self.ms}"
        def tik(self):
            self.ms +=1
class _color:
    class HexToRgb:
        def __init__(self, hexCode):
            self.hexCode = hexCode
        @property
        def rgb(self):
            return self.__rgb
        @rgb.setter
        def rgb(self, rgb):
            self.__rgb = rgb
        @property
        def hexCode(self):
            return self.__hexCode
        @hexCode.setter
        def hexCode(self, hexCode):
            hexCode = hexCode.replace('#', '')
            self.__hexCode = hexCode
            self.runApp()
        def runApp(self):
            self.rgb = tuple(int(self.hexCode[i:i+2], 16) for i in (0, 2, 4))
        def __repr__(self):
            return f"{self.rgb[0]}, {self.rgb[1]}, {self.rgb[2]}"
    class RgbToHex:
        def __init__(self, rgb):
            self.rgb = rgb
        @property
        def rgb(self):
            return self.__rgb
        @rgb.setter
        def rgb(self,rgb):
            for i in range(3):
                if rgb[i] >= 256:
                    rgb[i] = 0
            self.__rgb = rgb
        def runApp(self):
            return '#%02x%02x%02x' % (self.rgb[0], self.rgb[1], self.rgb[2])
        def __repr__(self):
            return self.runApp()
        def __str__(self):
            return self.runApp()
if __name__ == "__main__":
    print("Github: https://github.com/pooriaahmadi/mpe")
    print("Youtube: https://www.youtube.com/channel/UCJd8Q9A-fyIpajhLvCvjViA")
    print("Discord: https://discord.gg/F6MV4Pu5mu")
    print("Please import this utility in your code using `import makepythoneasier`")
