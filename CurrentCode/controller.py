from robot import Robot

class Controller:
    def __init__(self, Robot):
        self.robot = Robot
        self.xprec = Robot.x
        self.yprec = Robot.y
        self.distance_parcourue = 0
