from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

hoveel = 9

for _ in range(5):
    robotArm.grab()
    for _ in range(hoveel):
        robotArm.moveRight()
    robotArm.drop()
    hoveel -=1
    for _ in range (hoveel):
        robotArm.moveLeft()
    hoveel -=1

robotArm.wait()