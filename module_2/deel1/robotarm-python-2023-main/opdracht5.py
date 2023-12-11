from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')


for arm in range(7):
    robotArm.moveRight()
for arm in range(7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    for arm in range(2):
        robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()


robotArm.wait()