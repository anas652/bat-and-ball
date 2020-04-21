import tkinter
import time

canvasWidth = 750
canvasHeight = 500
window = tkinter.Tk()
canvas = tkinter.Canavas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()

bat = canvas.create_rectangle(0, 0, 40, 10, fill = "dark turqoise")
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
	global leftPressed, righttPressed
	if event.keysym == "Left":
		leftPressed = 1
	elif event.keysym == "Right":
		rightPressed = 1


def on_key_release(event):
	global leftPressed, RightPressed
	if event.keysym == "Left":
		LeftPressed = 0
	elif event.keysym == "right":
		rightPressed = 0
