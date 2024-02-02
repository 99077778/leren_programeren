from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')


# robotArm.scan = str(robotArm.scan)

# for _ in range(9):
#     robotArm.scan()
#     if robotArm.scan == 'white':
#         robotArm.grab()
#     else:
#         robotArm.moveRight()





# for _ in range(9):
#     color = robotArm.scan()
#     if color == 'white':
#         robotArm.grab()
#     else:
#         robotArm.moveRight()






for _ in range(8):
    robotArm.moveRight()

for n in range(9):
    robotArm.grab()
    colour = robotArm.scan()
    if colour == 'white':
        robotArm.moveRight()
        robotArm.drop()
        if n < 8:
            robotArm.moveLeft()
            robotArm.moveLeft()
    else:
        robotArm.drop()
        if n < 8:
            robotArm.moveLeft()

robotArm.wait()