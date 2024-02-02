from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
hoveel = 5


counter = 0

for _ in range(3):
    robotArm.moveRight()

for _ in range(10):
    robotArm.grab()
    for _ in range(5):
        robotArm.moveRight()
    robotArm.drop()
    counter = counter +1
    if counter == 4 or counter == 7 or counter == 9:
        hoveel +=1
    if counter == 5 or counter == 8 or counter == 10:
        hoveel = hoveel - 1
    for _ in range(hoveel):
        robotArm.moveLeft()
    
        
        

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()