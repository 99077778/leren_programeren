from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

hoveel = 9

for n in range(9):
    robotArm.grab()
    colour = robotArm.scan()
    if colour == 'red':
        for _ in range(hoveel):
            robotArm.moveRight()
        robotArm.drop()
        hoveel -= 1
        for _ in range(hoveel):
            robotArm.moveLeft()        
    else:
        robotArm.drop()
        robotArm.moveRight()
        hoveel -= 1

robotArm.wait()
