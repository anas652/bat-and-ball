import tkinter
import time

canvasWidth = 750
canvasHeight = 500
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()

bat = canvas.create_rectangle(0, 0, 40, 10, fill = "dark turquoise")
ball = canvas.create_oval(0, 0, 10, 10, fill = "deep pink")

windowOpen = True

def main_loop():
	while windowOpen == True:
		move_bat()
		move_ball()
		window.update()
		time.sleep(0.02)
		if windowOpen == True:
			check_game_over()

leftPressed = 0
rghitPressed = 0

def on_key_pressed(event):
	global leftPressed, rightPressed
	if event.keysym == "Left":
		leftPressed = 1
	elif event.keysym == "Right":
		rightPressed = 1
   
def on_key_release(event):
	global leftPressed, rightPressed
	if event.keysym == "Left":
		leftPressed = 0
	elif event.keysym == "right":
		rightPressed = 0

batSpeed = 6
def move_bat():
	batMove = batSpeed*rightPressed - batSpeed*leftPressed 
	(batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
	if (batLeft > 0) and (batRight < canvasWidth or batMove < 0):
		canvas.move(bat, batMove, 0)

ballMoveX = 4
ballMoveY = -4
setBatTop = canvasHeight-40
setBatBottom = canvasHeight-30

def move_ball():
	global ballMoveX, ballMoveY
	(ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
	if ballMoveX > 0 and ballRight > canvasWidth:
		ballMovex = -ballMoveX
	if ballMoveX < 0 and ballLeft < 0:
		balMoveX = -ballMoveX
	if ballMoveY < 0 and ballTop < 0:
		ballMoveY = -ballMoveY
	if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
		(batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
		if ballRight > batLeft and ballLeft < batRight:
			ballMoveY = -ballMoveY
	canvas.move(ball, ballMovex, ballMoveY)

def check_game_over():
	(batLeft, ballTop, ballBottom) = canvas.coords(ball)
	if ballTop > canvasHeight:
		playAgain = tkinter.messagebox.askesno(message = "Do you want to play again?" )
		if playAgain == True:
			reset()
		else:
			close()

def close():
	global windowOpen
	windowOpen = False
	window.destroy()


