from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')


# robotArm.scan = str(robotArm.scan)

# for _ in range(9):
#     robotArm.scan()
#     if robotArm.scan == 'white':
#         robotArm.grab()
#     else:
#         robotArm.moveRight()



for _ in range(9):
    color = robotArm.scan()
    if color == 'white':
        robotArm.grab()
    else:
        robotArm.moveRight()


robotArm.wait()