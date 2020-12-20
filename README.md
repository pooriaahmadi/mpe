# *M*ake*P*ython*E*asier, MPE##
### Usefull Python utility for coding and use classes for making python easier to use and code
## Features:
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
	Usage: var = import._turtle()
	- Functions:
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
