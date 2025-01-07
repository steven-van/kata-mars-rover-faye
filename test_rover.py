class Rover:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 'NORTH'

    def executeCommands(self, commands):
        for command in commands:
            if command == 'f':
                self.moveForward()
            if command == 'b':
                self.moveBackward()
            if command == 'l':
                self.turnLeft()
            if command == 'r':
                self.turnRight()
    
    def moveForward(self):
        if self.direction == 'NORTH':
            self.y += 1
        elif self.direction == 'SOUTH':
            self.y -= 1
        elif self.direction == 'WEST':
            self.x -= 1
        elif self.direction == 'EAST':
            self.x += 1
    def moveBackward(self):
        if self.direction == 'NORTH':
            self.y -= 1
        elif self.direction == 'SOUTH':
            self.y += 1
        elif self.direction == 'WEST':
            self.x += 1
        elif self.direction == 'EAST':
            self.x -= 1
    def turnRight(self):
        self.direction = 'EAST'
    def turnLeft(self):
        self.direction = 'WEST'

def test_rover_moves_forward():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command f
    rover.executeCommands(['f'])
    
    # Then : The rover moves to position (0,1)
    assert rover.x == 0
    assert rover.y == 1
    
def test_rover_moves_backward():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command b
    rover.executeCommands(['b'])
    
    # Then : The rover moves to position (0,-1) and still faces North
    assert rover.x == 0
    assert rover.y == -1
    assert rover.direction == 'NORTH'
    
def test_rover_turns_left():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command l
    rover.executeCommands(['l'])

    # Then : The rover faces West
    assert rover.direction == 'WEST'

def test_rover_turns_right():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command r
    rover.executeCommands(['r'])
    
    # Then : The rover faces East
    assert rover.direction == 'EAST'

def test_rover_turns_left_and_forward():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command l, f
    rover.executeCommands(['l'])
    rover.executeCommands(['f'])

    # Then : The rover faces West and moves to position (-1,0)
    assert rover.x == -1
    assert rover.y == 0
    assert rover.direction == 'WEST'


def test_rover_turns_right_and_forward():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command r, f
    rover.executeCommands(['r'])
    rover.executeCommands(['f'])

    # Then : The rover faces East and moves to position (1,0)
    assert rover.x == 1
    assert rover.y == 0
    assert rover.direction == 'EAST'
