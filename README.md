# *M*ake*P*ython*E*asier, MPE
### Usefull Python utility for coding and use classes for making python easier to use and code
***Please don't sell this Utility***
- This Library/Utility has been developed by Pooria Ahmadi and feel free to edit it and use it easily :), If you want, you can send me the edited version and let me add the edited ones to base library and mention you in the main file.
- Discord: https://discord.gg/F6MV4Pu5mu
- Github: https://github.com/pooriaahmadi
- Youtube: https://www.youtube.com/channel/UCJd8Q9A-fyIpajhLvCvjViA
## Features:
***ALL CLASSES HAVE DEAFULT VALUE*** You can import empty and use default values
- Turtle
- Math
	- Fractions
- Random
	- RandomNumber
	- RandomNumbers
	- RandomCharacter
	- RandomCharacters
	- RandomNumberAndCharacters
- Time
	- Clock(hh:mm:ss:ms)
	- Date(M/D/Y)
- Color
	- HexToRgb
	- RgbToHex
## Documention:
- Turtle:
	- 
	Usage: import._turtle()
	- Functions:
		- Usage: import._turtle.FUNCTIONNAME()
		- createShape(sides, sideLength, isRandom) 
			- sides: Sides of shape, Ex. Triangle = 3
			- sideLength: Each side length, Ex. 100
			- isRandom: Random Color for the shape, Ex. True
		- createMaze(times, degree, isRandom)
			- times: times for repeating fucntion, Ex. 500
			- degree: degree of shape from 180, Ex. Triangle = 120
			- isRandom: Random Color for the shape, Ex. True
		- setSpeed(newSpeed)
			- newSpeed: Speed of the pen(0=unlimited), Ex. 1
		- setColor(color, isRandom)
			- color: color in rgb mode(tuple), Ex. setColor((255,0,0))
			- isRandom: Random Color for the shape, Ex. True
		- setPos(x, y, isDown)
			- isDown: determine pen is up or down, Ex. True
		- forward(length, isDown)
			- length: length for going forward
			- isDown: determine pen is up or down, Ex. True
		- backward(length, isDown)
			- length: length for going backward
			- isDown: determine pen is up or down, Ex. True
		- up()
		- down()
		- left(degree):
			- degree: degree for turning left from 180
		- right(degree):
			- degree: degree for turning right from 180
- Math:
	- 
	- Usage: import._math()
	- Classes:
		- Fraction:
			- Usage: import._math.fraction(f1, f2)
			- Functions:
				- import._math.fraction(f1, f2)
					- f1: numerator
					- f2: denominator
				- abs
				- add
				- sub
				- neg
				- mul
				- invert
				- eq
				- lt
				- le
				- bt
				- be
- Random:
	-
	- Usage: import._random()
	- Classes:
		- Usage: import._random.CLASSNAME()
		- randomNumber(startNumber, endNumber)
			- startNumber: starting number of the cycle
			- endNumber: ending number of the cycle
		- randomNumbers(length):
			- length: length of int
		- randomCharacter(startChar, endChar)
			- startChar: starting character in the cycle
			- endChar: ending character in the cycle
		- randomCharacters(length, startChar, endChar):
			- length: length of string
			- startChar: starting character in the cycle
			- endChar: ending character in the cycle
		- randomNumbersAndCharacters(length):
			- length: length of string
- Time
	- 
	- Usage: import._time()
	- Classes:
		- Usage: import._time.CLASSNAME()
		- date(day, month, year):
			- int Please
			- Functions:
				- tik()
					- Description: will add 1 day to the date
		- time(ms, second, minute, hour)
			- int Please
			- Functions:
				- Description: will add 1ms to the ms
- Color:
	- 
	- Usage: import._color()
	- Classes:
		- Usage: import._color.CLASSNAME
		- HexToRgb(hexCode)
			- hexCode: hexCode in string
		- RgbToHex(rgb)
			- rgb: rgb in tuple, Ex. (255,0,0)
