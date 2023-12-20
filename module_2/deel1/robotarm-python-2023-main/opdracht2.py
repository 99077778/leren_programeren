from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')
robotArm.grab()
for arm in range(9):
    robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()
for arm in range(5):
    robotArm.moveLeft()
robotArm.grab()
for arm in range(5):
    robotArm.moveRight()
robotArm.drop()



robotArm.wait()