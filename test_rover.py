class Rover:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def executeCommands(self, commands):
        for command in commands:
            if command == 'f':
                self.moveForward()
    
    def moveForward(self):
        self.y += 1

def test_rover_moves_forward():
    # Given : The rover is at position (0,0) facing North
    rover = Rover(0, 0)
    
    # When : The rover receives the command f
    rover.executeCommands(['f'])
    
    # Then : The rover moves to position (0,1)
    assert rover.x == 0, f"Expected x=0, got {rover.x}"
    assert rover.y == 1, f"Expected y=1, got {rover.y}"