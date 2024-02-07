from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)



hoveel = 1

for _ in range(7):
    robotArm.grab()
    colour = robotArm.scan()
    if colour:
        for _ in range(hoveel):
            robotArm.moveRight()
        
        robotArm.drop()
        for _ in range(hoveel):
            robotArm.moveLeft()
        hoveel +=1
    else:
        break



robotArm.wait()