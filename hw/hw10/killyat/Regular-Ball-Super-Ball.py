class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# Example usage
if __name__ == "__main__":
    ball1 = Ball()
    ball2 = Ball("super")
    
    print(ball1.ball_type)
    print(ball2.ball_type)