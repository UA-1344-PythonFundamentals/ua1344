class Ball(object):
    def __init__(self, type="regular"):
        self.type = type
        
ball1 = Ball()
ball2 = Ball("super")

print(ball1.type)
print(ball2.type) 