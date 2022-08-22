import turtle
import random
import time

grid = ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y", "Y", "Y", "Y", "Y", "Y"]
screen = turtle.Screen()
screen.setup(600,600)
ship1hits = 0
ship2hits = 0
ship3hits = 0
ship4hits = 0
ship5hits = 0
shipAsunk = False
shipBsunk = False
shipCsunk = False
shipDsunk = False
shipEsunk = False



pen = turtle.Turtle()
pen.speed(100)
pen.penup()
pen.goto(-400, 375)
pen.pendown()
pen.forward(800)
pen.right(90)
pen.forward(750)
pen.right(90)
pen.forward(800)
pen.right(90)
pen.forward(750)
pen.goto(-240, 375)
pen.right(180)
pen.forward(750)
pen.penup()
pen.goto(-80, 375)
pen.pendown()
pen.forward(750)
pen.penup()
pen.goto(80, 375)
pen.pendown()
pen.forward(750)
pen.penup()
pen.goto(240, 375)
pen.pendown()
pen.forward(750)
pen.penup()
pen.goto(-400, 225)
pen.left(90)
pen.pendown()
pen.forward(800)
pen.penup()
pen.goto(-400, 75)
pen.pendown()
pen.forward(800)
pen.penup()
pen.goto(-400, -75)
pen.pendown()
pen.forward(800)
pen.penup()
pen.goto(-400, -225)
pen.pendown()
pen.forward(800)
#
pen.penup()
pen.goto(-450, 300)
pen.pendown()
pen.write("A", move=False,align='left', font=('Arial', 30, 'normal'))
pen.penup()
pen.goto(-450, 150)
pen.pendown()
pen.write("B", move=False,align='left', font=('Arial', 30, 'normal'))
pen.penup()
pen.goto(-450, 0)
pen.pendown()
pen.write("C", move=False,align='left', font=('Arial', 30, 'normal'))
pen.penup()
pen.goto(-450, -150)
pen.pendown()
pen.write("D", move=False,align='left', font=('Arial', 30, 'normal'))
pen.penup()
pen.goto(-450, -300)
pen.pendown()
pen.write("E", move=False,align='left', font=('Arial', 30, 'normal'))
#
pen.penup()
pen.goto(-325, 380)
pen.pendown()
pen.write("1", move=False,align='left', font=('Arial', 30, 'normal'))
pen.penup()
pen.goto(-150, 380)
pen.pendown()
pen.write("2", move=False,align='left', font=('Arial', 30, 'normal'))
pen.penup()
pen.goto(0, 380)
pen.pendown()
pen.write("3", move=False,align='left', font=('Arial', 30, 'normal'))
pen.penup()
pen.goto(150, 380)
pen.pendown()
pen.write("4", move=False,align='left', font=('Arial', 30, 'normal'))
pen.penup()
pen.goto(300, 380)
pen.pendown()
pen.write("5", move=False,align='left', font=('Arial', 30, 'normal'))

def shipLocation():
  global grid
  ship1 = random.randint(1, 25)
  ship2 = random.randint(1, 25)
  ship3 = random.randint(1, 24)
  ship4 = random.randint(1, 25)
  ship5 = random.randint(1, 24)
  ship5_direction= random.randint(0,1)
  ship3_direction= random.randint(0,1)
#ship A
  if ship1 == 1:
    grid[0] = "A"
  elif ship1 == 2:
    grid[1] = "A"
  elif ship1 == 3:
    grid[2] = "A"
  elif ship1 == 4:
    grid[3] = "A"
  elif ship1 == 5:
    grid[4] = "A"
  elif ship1 == 6:
    grid[5] = "A"
  elif ship1 == 7:
    grid[6] = "A"
  elif ship1 == 8:
    grid[7] = "A"   
  elif ship1 == 9:
    grid[8] = "A"
  elif ship1 == 10:
    grid[9] = "A"
  elif ship1 == 11:
    grid[10] = "A"
  elif ship1 == 12:
    grid[11] = "A"
  elif ship1 == 13:
    grid[12] = "A"
  elif ship1 == 14:
    grid[13] = "A"
  elif ship1 == 15:
    grid[14] = "A"
  elif ship1 == 16:
    grid[15] = "A"
  elif ship1 == 17:
    grid[16] = "A"
  elif ship1 == 18:
    grid[17] = "A"
  elif ship1 == 19:
    grid[18] = "A"
  elif ship1 == 20:
    grid[19] = "A"
  elif ship1 == 21:
    grid[20] = "A"
  elif ship1 == 22:
    grid[21] = "A"
  elif ship1 == 23:
    grid[22] = "A"
  elif ship1 == 24:
    grid[23] = "A"
  elif ship1 == 25:
    grid[24] = "A"
#ship B
  if ship2 == 1:
    grid[0] = "B"
  elif ship2 == 2:
    grid[1] = "B"
  elif ship2 == 3:
    grid[2] = "B"
  elif ship2 == 4:
    grid[3] = "B"
  elif ship2 == 5:
    grid[4] = "B"
  elif ship2 == 6:
    grid[5] = "B"
  elif ship2 == 7:
    grid[6] = "B"
  elif ship2 == 8:
    grid[7] = "B"   
  elif ship2 == 9:
    grid[8] = "B"
  elif ship2 == 10:
    grid[9] = "B"
  elif ship2 == 11:
    grid[10] = "B"
  elif ship2 == 12:
    grid[11] = "B"
  elif ship2 == 13:
    grid[12] = "B"
  elif ship2 == 14:
    grid[13] = "B"
  elif ship2 == 15:
    grid[14] = "B"
  elif ship2 == 16:
    grid[15] = "B"
  elif ship2 == 17:
    grid[16] = "B"
  elif ship2 == 18:
    grid[17] = "B"
  elif ship2 == 19:
    grid[18] = "B"
  elif ship2 == 20:
    grid[19] = "B"
  elif ship2 == 21:
    grid[20] = "B"
  elif ship2 == 22:
    grid[21] = "B"
  elif ship2 == 23:
    grid[22] = "B"
  elif ship2 == 24:
    grid[23] = "B"
  elif ship2 == 25:
    grid[24] = "B"
#ShipD
  if ship4 == 1:
    grid[0] = "D"
  elif ship4 == 2:
    grid[1] = "D"
  elif ship4 == 3:
    grid[2] = "D"
  elif ship4 == 4:
    grid[3] = "D"
  elif ship4 == 5:
    grid[4] = "D"
  elif ship4 == 6:
    grid[5] = "D"
  elif ship4 == 7:
    grid[6] = "D"
  elif ship4 == 8:
    grid[7] = "D"   
  elif ship4 == 9:
    grid[8] = "D"
  elif ship4 == 10:
    grid[9] = "D"
  elif ship4 == 11:
    grid[10] = "D"
  elif ship4 == 12:
    grid[11] = "D"
  elif ship4 == 13:
    grid[12] = "D"
  elif ship4 == 14:
    grid[13] = "D"
  elif ship4 == 15:
    grid[14] = "D"
  elif ship4 == 16:
    grid[15] = "D"
  elif ship4 == 17:
    grid[16] = "D"
  elif ship4 == 18:
    grid[17] = "D"
  elif ship4 == 19:
    grid[18] = "D"
  elif ship4 == 20:
    grid[19] = "D"
  elif ship4 == 21:
    grid[20] = "D"
  elif ship4 == 22:
    grid[21] = "D"
  elif ship4 == 23:
    grid[22] = "D"
  elif ship4 == 24:
    grid[23] = "D"
  elif ship4 == 25:
    grid[24] = "D"
#shipC vertical
  if ship3_direction == 1:
    ship3 = random.randint(1, 20)
    if ship3 == 1:
      grid[0] = "C"
      grid[5] = "C"
    elif ship3 == 2:
      grid[1] = "C"
      grid[6] = "C"
    elif ship3 == 3:
      grid[2] = "C"
      grid[7] = "C"
    elif ship3 == 4:
      grid[3] = "C"
      grid[8] = "C" 
    elif ship3 == 5:
      grid[4] = "C"
      grid[9] = "C"
    elif ship3 == 6:
      grid[5] = "C"
      grid[10] = "C"
    elif ship3 == 7:
      grid[6] = "C"
      grid[11] = "C"
    elif ship3 == 8:
      grid[7] = "C"
      grid[12] = "C"
    elif ship3 == 9:
      grid[8] = "C"
      grid[13] = "C"
    elif ship3 == 10:
      grid[9] = "C"
      grid[14] = "C"
    elif ship3 == 11:
      grid[10] = "C"
      grid[15] = "C"
    elif ship3 == 12:
      grid[11] = "C"
      grid[16] = "C"
    elif ship3 == 13:
      grid[12] = "C"
      grid[17] = "C"
    elif ship3 == 14:
      grid[13] = "C"
      grid[18] = "C"
    elif ship3 == 15:
      grid[14] = "C"
      grid[19] = "C"
    elif ship3 == 16:
      grid[20] = "C"
      grid[25] = "C"
    elif ship3 == 17:
      grid[21] = "C"
      grid[26] = "C"
    elif ship3 == 18:
      grid[22] = "C"
      grid[27] = "C"
    elif ship3 == 19:
      grid[23] = "C"
      grid[28] ="C"
    elif ship3 == 20:
      grid[24] = "C"
      grid[29] = "C"
#shipC horizontal
  if ship3_direction == 0:
    if ship3 == 1:
      grid[0] = "C"
      grid[1] = "C"
    elif ship3 == 2:
      grid[1] = "C"
      grid[2] = "C"
    elif ship3 == 3:
      grid[2] = "C"
      grid[3] = "C"
    elif ship3 == 4:
      grid[3] = "C"
      grid[4] = "C"
    elif ship3 == 5:
      grid[5] = "C"
      grid[6] = "C"
    elif ship3 == 6:
      grid[6] = "C"
      grid[7] = "C"
    elif ship3 == 7:
      grid[7] = "C"
      grid[8] = "C"
    elif ship3 == 8:
      grid[8] = "C"
      grid[9] = "C"
    elif ship3 == 9:
      grid[10] = "C"
      grid[11] = "C"
    elif ship3 == 10:
      grid[11] = "C"
      grid[12] = "C"
    elif ship3 == 11:
      grid[12] = "C"
      grid[13] = "C"
    elif ship3 == 12:
      grid[13] = "C"
      grid[14] = "C"
    elif ship3 == 13:
      grid[15] = "C"
      grid[16] = "C"
    elif ship3 == 14:
      grid[16] = "C"
      grid[17] = "C"
    elif ship3 == 15:
      grid[17] = "C"
      grid[18] = "C"
    elif ship3 == 16:
      grid[18] = "C"
      grid[19] = "C"
    elif ship3 == 17:
      grid[20] = "C"
      grid[21] = "C"
    elif ship3 == 18:
      grid[21] = "C"
      grid[22] = "C"
    elif ship3 == 19:
      grid[22] = "C"
      grid[23] = "C"
    elif ship3 == 20:
      grid[23] = "C"
      grid[24] = "C"
    elif ship3 == 21:
      grid[25] = "C"
      grid[26] = "C"
    elif ship3 == 22:
      grid[26] = "C"
      grid[27] = "C"
    elif ship3 == 23:
      grid[27] = "C"
      grid[28] = "C"
    elif ship3 == 24:
      grid[28] = "C"
      grid[29] = "C"
#Ship E Vertical
  if ship5_direction == 1:
    ship5 = random.randint(1, 20)
    if ship5 == 1:
      grid[0] = "E"
      grid[5] = "E"
    elif ship5 == 2:
      grid[1] = "E"
      grid[6] = "E"
    elif ship5 == 3:
      grid[2] = "E"
      grid[7] = "E"
    elif ship5 == 4:
      grid[3] = "E"
      grid[8] = "E" 
    elif ship5 == 5:
      grid[4] = "E"
      grid[9] = "E"
    elif ship5 == 6:
      grid[5] = "E"
      grid[10] = "E"
    elif ship5 == 7:
      grid[6] = "E"
      grid[11] = "E"
    elif ship5 == 8:
      grid[7] = "E"
      grid[12] = "E"
    elif ship5 == 9:
      grid[8] = "E"
      grid[13] = "E"
    elif ship5 == 10:
      grid[9] = "E"
      grid[14] = "E"
    elif ship5 == 11:
      grid[10] = "E"
      grid[15] = "E"
    elif ship5 == 12:
      grid[11] = "E"
      grid[16] = "E"
    elif ship5 == 13:
      grid[12] = "E"
      grid[17] = "E"
    elif ship5 == 14:
      grid[13] = "E"
      grid[18] = "E"
    elif ship5 == 15:
      grid[14] = "E"
      grid[19] = "E"
    elif ship5 == 16:
      grid[20] = "E"
      grid[25] = "E"
    elif ship5 == 17:
      grid[21] = "E"
      grid[26] = "E"
    elif ship5 == 18:
      grid[22] = "E"
      grid[27] = "E"
    elif ship5 == 19:
      grid[23] = "E"
      grid[28] ="E"
    elif ship5 == 20:
      grid[24] = "E"
      grid[29] = "E"
#Ship E Horizontal
  if ship5_direction == 0:
    if ship5 == 1:
      grid[0] = "E"
      grid[1] = "E"
    elif ship5 == 2:
      grid[1] = "E"
      grid[2] = "E"
    elif ship5 == 3:
      grid[2] = "E"
      grid[3] = "E"
    elif ship5 == 4:
      grid[3] = "E"
      grid[4] = "E"
    elif ship5 == 5:
      grid[5] = "E"
      grid[6] = "E"
    elif ship5 == 6:
      grid[6] = "E"
      grid[7] = "E"
    elif ship5 == 7:
      grid[7] = "E"
      grid[8] = "E"
    elif ship5 == 8:
      grid[8] = "E"
      grid[9] = "E"
    elif ship5 == 9:
      grid[10] = "E"
      grid[11] = "E"
    elif ship5 == 10:
      grid[11] = "E"
      grid[12] = "E"
    elif ship5 == 11:
      grid[12] = "E"
      grid[13] = "E"
    elif ship5 == 12:
      grid[13] = "E"
      grid[14] = "E"
    elif ship5 == 13:
      grid[15] = "E"
      grid[16] = "E"
    elif ship5 == 14:
      grid[16] = "E"
      grid[17] = "E"
    elif ship5 == 15:
      grid[17] = "E"
      grid[18] = "E"
    elif ship5 == 16:
      grid[18] = "E"
      grid[19] = "E"
    elif ship5 == 17:
      grid[20] = "E"
      grid[21] = "E"
    elif ship5 == 18:
      grid[21] = "E"
      grid[22] = "E"
    elif ship5 == 19:
      grid[22] = "E"
      grid[23] = "E"
    elif ship5 == 20:
      grid[23] = "E"
      grid[24] = "E"
    elif ship5 == 21:
      grid[25] = "E"
      grid[26] = "E"
    elif ship5 == 22:
      grid[26] = "E"
      grid[27] = "E"
    elif ship5 == 23:
      grid[27] = "E"
      grid[28] = "E"
    elif ship5 == 24:
      grid[28] = "E"
      grid[29] = "E"
def attack():
  global grid
  global ship1hits
  global ship2hits
  global ship3hits
  global ship4hits
  global ship5hits
  attack_letter = input("which letter do you want to attack")
  attack_number = input("which number do you want to attack")
  if attack_letter == "A":
    if attack_number == "1":
      print("attacking")
      if grid[0] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-375, 225)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[0] != "Y":
        pen.penup()
        pen.goto(-375, 225)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[0] == "A":
          print ("HIT SHIP A")
          grid[0] == "Y"
          ship1hits += 1
        if grid[0] == "B":
          print ("HIT SHIP B")
          grid[0] == "Y"
          ship2hits += 1
        if grid[0] == "C":
          print ("HIT SHIP C")
          grid[0] == "Y"
          ship3hits += 1
        if grid[0] == "D":
          print ("HIT SHIP D")
          grid[0] == "Y"
          ship4hits += 1
        if grid[0] == "E":
          print ("HIT SHIP E")
          grid[0] == "Y"
          ship5hits += 1
    if attack_number == "2":
      print("attacking")
      if grid[5] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-215, 225)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[5] != "Y":
        pen.penup()
        pen.goto(-215, 225)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[5] == "A":
          print ("HIT SHIP A")
          grid[5] == "Y"
          ship1hits += 1
        if grid[5] == "B":
          print ("HIT SHIP B")
          grid[5] == "Y"
          ship2hits += 1
        if grid[5] == "C":
          print ("HIT SHIP C")
          grid[5] == "Y"
          ship3hits += 1
        if grid[5] == "D":
          print ("HIT SHIP D")
          grid[5] == "Y"
          ship4hits += 1
        if grid[5] == "E":
          print ("HIT SHIP E")
          grid[5] == "Y"
          ship5hits += 1
    if attack_number == "3":
      print("attacking")
      if grid[10] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-55, 225)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[10] != "Y":
        pen.penup()
        pen.goto(-55, 225)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[10] == "A":
          print ("HIT SHIP A")
          grid[10] == "Y"
          ship1hits += 1
        if grid[10] == "B":
          print ("HIT SHIP B")
          grid[10] == "Y"
          ship2hits += 1
        if grid[10] == "C":
          print ("HIT SHIP C")
          grid[10] == "Y"
          ship3hits += 1
        if grid[10] == "D":
          print ("HIT SHIP D")
          grid[10] == "Y"
          ship4hits += 1
        if grid[10] == "E":
          print ("HIT SHIP E")
          grid[10] == "Y"
          ship5hits += 1
    if attack_number == "4":
      print("attacking")
      if grid[15] == "Y":
        print("miss")
        pen.penup()
        pen.goto(105, 225)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[15] != "Y":
        pen.penup()
        pen.goto(105, 225)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[15] == "A":
          print ("HIT SHIP A")
          grid[15] == "Y"
          ship1hits += 1
        if grid[15] == "B":
          print ("HIT SHIP B")
          grid[15] == "Y"
          ship2hits += 1
        if grid[15] == "C":
          print ("HIT SHIP C")
          grid[15] == "Y"
          ship3hits += 1
        if grid[15] == "D":
          print ("HIT SHIP D")
          grid[15] == "Y"
          ship4hits += 1
        if grid[15] == "E":
          print ("HIT SHIP E")
          grid[15] == "Y"
          ship5hits += 1
    if attack_number == "5":
      print("attacking")
      if grid[20] == "Y":
        print("miss")
        pen.penup()
        pen.goto(265, 225)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[20] != "Y":
        pen.penup()
        pen.goto(265, 225)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[20] == "A":
          print ("HIT SHIP A")
          grid[20] == "Y"
          ship1hits += 1
        if grid[20] == "B":
          print ("HIT SHIP B")
          grid[20] == "Y"
          ship2hits += 1
        if grid[20] == "C":
          print ("HIT SHIP C")
          grid[20] == "Y"
          ship3hits += 1
        if grid[20] == "D":
          print ("HIT SHIP D")
          grid[20] == "Y"
          ship4hits += 1
        if grid[20] == "E":
          print ("HIT SHIP E")
          grid[20] == "Y"
          ship5hits += 1
  if attack_letter == "B":
    if attack_number == "1":
      print("attacking")
      if grid[1] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-375, 65)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[1] != "Y":
        pen.penup()
        pen.goto(-375, 65)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[1] == "A":
          print ("HIT SHIP A")
          grid[1] == "Y"
          ship1hits += 1
        if grid[1] == "B":
          print ("HIT SHIP B")
          grid[1] == "Y"
          ship2hits += 1
        if grid[1] == "C":
          print ("HIT SHIP C")
          grid[1] == "Y"
          ship3hits += 1
        if grid[1] == "D":
          print ("HIT SHIP D")
          grid[1] == "Y"
          ship4hits += 1
        if grid[1] == "E":
          print ("HIT SHIP E")
          grid[1] == "Y"
          ship5hits += 1
    if attack_number == "2":
      print("attacking")
      if grid[6] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-215, 65)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[6] != "Y":
        pen.penup()
        pen.goto(-215, 65)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[6] == "A":
          print ("HIT SHIP A")
          grid[6] == "Y"
          ship1hits += 1
        if grid[6] == "B":
          print ("HIT SHIP B")
          grid[6] == "Y"
          ship2hits += 1
        if grid[6] == "C":
          print ("HIT SHIP C")
          grid[6] == "Y"
          ship3hits += 1
        if grid[6] == "D":
          print ("HIT SHIP D")
          grid[6] == "Y"
          ship4hits += 1
        if grid[6] == "E":
          print ("HIT SHIP E")
          grid[6] == "Y"
          ship5hits += 1
    if attack_number == "3":
      print("attacking")
      if grid[11] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-55, 65)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[11] != "Y":
        pen.penup()
        pen.goto(-55, 65)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[11] == "A":
          print ("HIT SHIP A")
          grid[11] == "Y"
          ship1hits += 1
        if grid[11] == "B":
          print ("HIT SHIP B")
          grid[11] == "Y"
          ship2hits += 1
        if grid[11] == "C":
          print ("HIT SHIP C")
          grid[11] == "Y"
          ship3hits += 1
        if grid[11] == "D":
          print ("HIT SHIP D")
          grid[11] == "Y"
          ship4hits += 1
        if grid[11] == "E":
          print ("HIT SHIP E")
          grid[11] == "Y"
          ship5hits += 1
    if attack_number == "4":
      print("attacking")
      if grid[16] == "Y":
        print("miss")
        pen.penup()
        pen.goto(105, 65)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[16] != "Y":
        pen.penup()
        pen.goto(105, 65)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[16] == "A":
          print ("HIT SHIP A")
          grid[16] == "Y"
          ship1hits += 1
        if grid[16] == "B":
          print ("HIT SHIP B")
          grid[16] == "Y"
          ship2hits += 1
        if grid[16] == "C":
          print ("HIT SHIP C")
          grid[16] == "Y"
          ship3hits += 1
        if grid[16] == "D":
          print ("HIT SHIP D")
          grid[16] == "Y"
          ship4hits += 1
        if grid[16] == "E":
          print ("HIT SHIP E")
          grid[16] == "Y"
          ship5hits += 1
    if attack_number == "5":
      print("attacking")
      if grid[21] == "Y":
        print("miss")
        pen.penup()
        pen.goto(265, 65)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[21] != "Y":
        pen.penup()
        pen.goto(265, 65)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[21] == "A":
          print ("HIT SHIP A")
          grid[21] == "Y"
          ship1hits += 1
        if grid[21] == "B":
          print ("HIT SHIP B")
          grid[21] == "Y"
          ship2hits += 1
        if grid[21] == "C":
          print ("HIT SHIP C")
          grid[21] == "Y"
          ship3hits += 1
        if grid[21] == "D":
          print ("HIT SHIP D")
          grid[21] == "Y"
          ship4hits += 1
        if grid[21] == "E":
          print ("HIT SHIP E")
          grid[21] == "Y"
          ship5hits += 1
  if attack_letter == "C":
    if attack_number == "1":
      print("attacking")
      if grid[2] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-375, -95)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[2] != "Y":
        pen.penup()
        pen.goto(-375, -95)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[2] == "A":
          print ("HIT SHIP A")
          grid[2] == "Y"
          ship1hits += 1
        if grid[2] == "B":
          print ("HIT SHIP B")
          grid[2] == "Y"
          ship2hits += 1
        if grid[2] == "C":
          print ("HIT SHIP C")
          grid[2] == "Y"
          ship3hits += 1
        if grid[2] == "D":
          print ("HIT SHIP D")
          grid[2] == "Y"
          ship4hits += 1
        if grid[2] == "E":
          print ("HIT SHIP E")
          grid[2] == "Y"
          ship5hits += 1
    if attack_number == "2":
      print("attacking")
      if grid[7] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-215, -95)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[7] != "Y":
        pen.penup()
        pen.goto(-215, -95)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[7] == "A":
          print ("HIT SHIP A")
          grid[7] == "Y"
          ship1hits += 1
        if grid[7] == "B":
          print ("HIT SHIP B")
          grid[7] == "Y"
          ship2hits += 1
        if grid[7] == "C":
          print ("HIT SHIP C")
          grid[7] == "Y"
          ship3hits += 1
        if grid[7] == "D":
          print ("HIT SHIP D")
          grid[7] == "Y"
          ship4hits += 1
        if grid[7] == "E":
          print ("HIT SHIP E")
          grid[7] == "Y"
          ship5hits += 1
    if attack_number == "3":
      print("attacking")
      if grid[12] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-55, -95)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[12] != "Y":
        pen.penup()
        pen.goto(-55, -95)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[12] == "A":
          print ("HIT SHIP A")
          grid[12] == "Y"
          ship1hits += 1
        if grid[12] == "B":
          print ("HIT SHIP B")
          grid[12] == "Y"
          ship2hits += 1
        if grid[12] == "C":
          print ("HIT SHIP C")
          grid[12] == "Y"
          ship3hits += 1
        if grid[12] == "D":
          print ("HIT SHIP D")
          grid[12] == "Y"
          ship4hits += 1
        if grid[12] == "E":
          print ("HIT SHIP E")
          grid[12] == "Y"
          ship5hits += 1
    if attack_number == "4":
      print("attacking")
      if grid[17] == "Y":
        print("miss")
        pen.penup()
        pen.goto(105, -95)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[17] != "Y":
        pen.penup()
        pen.goto(105, -95)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[17] == "A":
          print ("HIT SHIP A")
          grid[17] == "Y"
          ship1hits += 1
        if grid[17] == "B":
          print ("HIT SHIP B")
          grid[17] == "Y"
          ship2hits += 1
        if grid[17] == "C":
          print ("HIT SHIP C")
          grid[17] == "Y"
          ship3hits += 1
        if grid[17] == "D":
          print ("HIT SHIP D")
          grid[17] == "Y"
          ship4hits += 1
        if grid[17] == "E":
          print ("HIT SHIP E")
          grid[17] == "Y"
          ship5hits += 1
    if attack_number == "5":
      print("attacking")
      if grid[22] == "Y":
        print("miss")
        pen.penup()
        pen.goto(265, -95)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[22] != "Y":
        pen.penup()
        pen.goto(265, -95)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[22] == "A":
          print ("HIT SHIP A")
          grid[22] == "Y"
          ship1hits += 1
        if grid[22] == "B":
          print ("HIT SHIP B")
          grid[22] == "Y"
          ship2hits += 1
        if grid[22] == "C":
          print ("HIT SHIP C")
          grid[22] == "Y"
          ship3hits += 1
        if grid[22] == "D":
          print ("HIT SHIP D")
          grid[22] == "Y"
          ship4hits += 1
        if grid[22] == "E":
          print ("HIT SHIP E")
          grid[22] == "Y"
          ship5hits += 1
  if attack_letter == "D":
    if attack_number == "1":
      print("attacking")
      if grid[3] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-375, -235)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[3] != "Y":
        pen.penup()
        pen.goto(-375, -235)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[3] == "A":
          print ("HIT SHIP A")
          grid[3] == "Y"
          ship1hits += 1
        if grid[3] == "B":
          print ("HIT SHIP B")
          grid[3] == "Y"
          ship2hits += 1
        if grid[3] == "C":
          print ("HIT SHIP C")
          grid[3] == "Y"
          ship3hits += 1
        if grid[3] == "D":
          print ("HIT SHIP D")
          grid[3] == "Y"
          ship4hits += 1
        if grid[3] == "E":
          print ("HIT SHIP E")
          grid[3] == "Y"
          ship5hits += 1
    if attack_number == "2":
      print("attacking")
      if grid[8] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-215, -235)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[8] != "Y":
        pen.penup()
        pen.goto(-215, -235)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[8] == "A":
          print ("HIT SHIP A")
          grid[8] == "Y"
          ship1hits += 1
        if grid[8] == "B":
          print ("HIT SHIP B")
          grid[8] == "Y"
          ship2hits += 1
        if grid[8] == "C":
          print ("HIT SHIP C")
          grid[8] == "Y"
          ship3hits += 1
        if grid[8] == "D":
          print ("HIT SHIP D")
          grid[8] == "Y"
          ship4hits += 1
        if grid[8] == "E":
          print ("HIT SHIP E")
          grid[8] == "Y"
          ship5hits += 1
    if attack_number == "3":
      print("attacking")
      if grid[13] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-55, -235)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[13] != "Y":
        pen.penup()
        pen.goto(-55, -235)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[13] == "A":
          print ("HIT SHIP A")
          grid[13] == "Y"
          ship1hits += 1
        if grid[13] == "B":
          print ("HIT SHIP B")
          grid[13] == "Y"
          ship2hits += 1
        if grid[13] == "C":
          print ("HIT SHIP C")
          grid[13] == "Y"
          ship3hits += 1
        if grid[13] == "D":
          print ("HIT SHIP D")
          grid[13] == "Y"
          ship4hits += 1
        if grid[13] == "E":
          print ("HIT SHIP E")
          grid[13] == "Y"
          ship5hits += 1
    if attack_number == "4":
      print("attacking")
      if grid[18] == "Y":
        print("miss")
        pen.penup()
        pen.goto(105, -235)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[18] != "Y":
        pen.penup()
        pen.goto(105, -235)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[18] == "A":
          print ("HIT SHIP A")
          grid[18] == "Y"
          ship1hits += 1
        if grid[18] == "B":
          print ("HIT SHIP B")
          grid[18] == "Y"
          ship2hits += 1
        if grid[18] == "C":
          print ("HIT SHIP C")
          grid[18] == "Y"
          ship3hits += 1
        if grid[18] == "D":
          print ("HIT SHIP D")
          grid[18] == "Y"
          ship4hits += 1
        if grid[18] == "E":
          print ("HIT SHIP E")
          grid[18] == "Y"
          ship5hits += 1
    if attack_number == "5":
      print("attacking")
      if grid[23] == "Y":
        print("miss")
        pen.penup()
        pen.goto(265, -235)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[23] != "Y":
        pen.penup()
        pen.goto(265, -235)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[23] == "A":
          print ("HIT SHIP A")
          grid[23] == "Y"
          ship1hits += 1
        if grid[23] == "B":
          print ("HIT SHIP B")
          grid[23] == "Y"
          ship2hits += 1
        if grid[23] == "C":
          print ("HIT SHIP C")
          grid[23] == "Y"
          ship3hits += 1
        if grid[23] == "D":
          print ("HIT SHIP D")
          grid[23] == "Y"
          ship4hits += 1
        if grid[23] == "E":
          print ("HIT SHIP E")
          grid[23] == "Y"
          ship5hits += 1
  if attack_letter == "E":
    if attack_number == "1":
      print("attacking")
      if grid[4] == "Y":
        print("miss")
        pen.penup()
        pen.goto(-375, -375)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[4] != "Y":
        pen.penup()
        pen.goto(-375, -375)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[4] == "A":
          print ("HIT SHIP A")
          grid[4] == "Y"
          ship1hits += 1
        if grid[4] == "B":
          print ("HIT SHIP B")
          grid[4] == "Y"
          ship2hits += 1
        if grid[4] == "C":
          print ("HIT SHIP C")
          grid[4] == "Y"
          ship3hits += 1
        if grid[4] == "D":
          print ("HIT SHIP D")
          grid[4] == "Y"
          ship4hits += 1
        if grid[4] == "E":
          print ("HIT SHIP E")
          grid[4] == "Y"
          ship5hits += 1
    if attack_number == "2":
      print("attacking")
      if grid[9] == "Y":
        pen.penup()
        pen.goto(-215, -375)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[9] != "Y":
        pen.penup()
        pen.goto(-215, -375)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[9] == "A":
          print ("HIT SHIP A")
          grid[9] == "Y"
          ship1hits += 1
        if grid[9] == "B":
          print ("HIT SHIP B")
          grid[9] == "Y"
          ship2hits += 1
        if grid[9] == "C":
          print ("HIT SHIP C")
          grid[9] == "Y"
          ship3hits += 1
        if grid[9] == "D":
          print ("HIT SHIP D")
          grid[9] == "Y"
          ship4hits += 1
        if grid[9] == "E":
          print ("HIT SHIP E")
          grid[9] == "Y"
          ship5hits += 1
    if attack_number == "3":
      print("attacking")
      if grid[14] == "Y":
        pen.penup()
        pen.goto(-55, -375)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[14] != "Y":
        pen.penup()
        pen.goto(-55, -375)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[14] == "A":
          print ("HIT SHIP A")
          grid[14] == "Y"
          ship1hits += 1
        if grid[14] == "B":
          print ("HIT SHIP B")
          grid[14] == "Y"
          ship2hits += 1
        if grid[14] == "C":
          print ("HIT SHIP C")
          grid[14] == "Y"
          ship3hits += 1
        if grid[14] == "D":
          print ("HIT SHIP D")
          grid[14] == "Y"
          ship4hits += 1
        if grid[14] == "E":
          print ("HIT SHIP E")
          grid[14] == "Y"
          ship5hits += 1
    if attack_number == "4":
      print("attacking")
      if grid[19] == "Y":
        pen.penup()
        pen.goto(105, -375)
        pen.pendown()
        pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[19] != "Y":
        pen.penup()
        pen.goto(105, -375)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[19] == "A":
          print ("HIT SHIP A")
          grid[19] == "Y"
          ship1hits += 1
        if grid[19] == "B":
          print ("HIT SHIP B")
          grid[19] == "Y"
          ship2hits += 1
        if grid[19] == "C":
          print ("HIT SHIP C")
          grid[19] == "Y"
          ship3hits += 1
        if grid[19] == "D":
          print ("HIT SHIP D")
          grid[19] == "Y"
          ship4hits += 1
        if grid[19] == "E":
          print ("HIT SHIP E")
          grid[19] == "Y"
          ship5hits += 1
    if attack_number == "5":
      print("attacking")
      pen.penup()
      pen.goto(265, -375)
      pen.pendown()
      pen.write("O", move=False,align='left', font=('Arial', 100, 'normal'))
      if grid[24] != "Y":
        pen.penup()
        pen.goto(265, -375)
        pen.pendown()
        pen.write("X", move=False,align='left', font=('Arial', 100, 'normal'))
        if grid[24] == "A":
          print ("HIT SHIP A")
          grid[24] == "Y"
          ship1hits += 1
        if grid[24] == "B":
          print ("HIT SHIP B")
          grid[24] == "Y"
          ship2hits += 1
        if grid[24] == "C":
          print ("HIT SHIP C")
          grid[24] == "Y"
          ship3hits += 1
        if grid[24] == "D":
          print ("HIT SHIP D")
          grid[24] == "Y"
          ship4hits += 1
        if grid[24] == "E":
          print ("HIT SHIP E")
          grid[24] == "Y"
          ship5hits += 1
def outcome():
  global ship1hits
  global ship2hits
  global ship3hits
  global ship4hits
  global ship5hits
  global shipAsunk
  global shipBsunk
  global shipCsunk
  global shipDsunk
  global shipEsunk
  if ship1hits >= 1 and shipAsunk == False:
    print ("You sunk ship A")
    shipAsunk = True
  if ship2hits >= 1 and shipBsunk == False:
    print ("You sunk ship B")
    shipBsunk = True
  if ship3hits >= 2 and shipCsunk == False:
    print ("You sunk ship C")
    shipCsunk = True
  if ship4hits >= 1 and shipDsunk == False:
    print ("You sunk ship D")
    shipDsunk = True
  if ship5hits >= 2 and shipEsunk == False:
    print ("You sunk ship E")
    shipEsunk = True
  if shipAsunk and shipBsunk and shipCsunk and shipDsunk and shipEsunk:
    pen.clear()
    pen.penup()
    pen.goto(-575, 0)
    pen.pendown()
    pen.write("You Sunk All Of The Ships", move=False,align='left', font=('Arial', 100, 'normal'))
def count():
  count = 0
  A = 0
  while A < len(grid) - 1:
    if grid[A] != "Y":
      count += 1
    A += 1
  print(count)

def gameLogic():
  count()
  shipLocation()
  while True:
    attack()
    time.sleep(5)
    outcome()

gameLogic()
