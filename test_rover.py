class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y

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
        self.y += 1
    def moveBackward(self):
        self.y -= 1
    def turnRight(self):
        self.x += 1
    def turnLeft(self):
        self.x -= 1

def test_rover_moves_forward():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command f
    rover.executeCommands(['f'])
    
    # Then : The rover moves to position (0,1)
    assert rover.x == 0, f"Expected x=0, got {rover.x}"
    assert rover.y == 1, f"Expected y=1, got {rover.y}"
    
def test_rover_moves_backward():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command b
    rover.executeCommands(['b'])
    
    # Then : The rover moves to position (0,-1)
    assert rover.x == 0, f"Expected x=0, got {rover.x}"
    assert rover.y == -1, f"Expected y=-1, got {rover.y}"
    
def test_rover_turns_left():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command l
    rover.executeCommands(['l'])
    
    # Then : The rover moves to position (-1,0)
    assert rover.x == -1, f"Expected x=-1, got {rover.x}"
    assert rover.y == 0, f"Expected y=0, got {rover.y}"

def test_rover_turns_right():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command r
    rover.executeCommands(['r'])
    
    # Then : The rover moves to position (1,0)
    assert rover.x == 1, f"Expected x=-1, got {rover.x}"
    assert rover.y == 0, f"Expected y=0, got {rover.y}"