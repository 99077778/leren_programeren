from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
for arm in range(4):
    print(arm)
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if arm < 3:
        robotArm.moveLeft()



# robotArm.grab()
# robotArm.moveRight()
# robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()