from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
hoveel = 5


counter = 0


for _ in range(10):
    robotArm.grab()
    for _ in range(5):
        robotArm.moveRight()
    robotArm.drop()
    counter = counter +1
    if counter == 1 or counter == 3 or counter == 6:
        hoveel = hoveel - 1
    if counter == 2 or counter == 4 or counter == 7:
        hoveel = hoveel +1
    for _ in range(hoveel):
        #print(hoveel)
        robotArm.moveLeft()
    
        
        

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()