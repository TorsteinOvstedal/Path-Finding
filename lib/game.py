import pygame

class Game:
    '''
        A barebones 'framework' for prototyping game concepts.
        Provides a simple top level game loop w/hooks into it.
        Hooks: init, input, update, render, stop.
        Entry point: start(resolution).
    '''

    def __init__(self):
        self.display = pygame.display
        self.events = pygame.event
        self.clock = pygame.time.Clock()
        self.ups = 60

    def _init(self, resolution):
        self.display.init()
        self.framebuffer = self.display.set_mode(resolution)
        self.init()

    def start(self, resolution=(960, 720)):
        self._init(resolution)

        self.running = True

        while self.running:
            self.clock.tick(self.ups)
            dt = self.clock.get_time()
            
            self.input()
            self.update(dt)
            self.render()
            
            self.events.pump()

    def init(self):
        # Skeleton implementation.
        self.clear_color = 0x000000

    def stop(self):
        # Skeleton implementation.
        self.running = False

    def input(self):
        # Skeleton implementation.
        if self.events.peek(pygame.QUIT):
            self.stop()

    def update(self, deltaTime: float):
        pass

    def render(self):
        # Skeleton implementation.
        self.framebuffer.fill(self.clear_color)
        pygame.display.flip()


class Demo(Game):

    class Ball:
        def __init__(self):
            self.pos = pygame.Vector2(0, 0)
            self.vel = pygame.Vector2(0.5, -0.5)
            self.r = 8
            self.c = 0xff0000
        
        def move(self, dt):
            self.pos += self.vel * dt
        
        def draw(self, buffer):
            pygame.draw.circle(buffer, self.c, self.pos, self.r)

    def init(self):
        self.clear_color = 0x000000
        self.ball = Demo.Ball()

    def update(self, dt):
        ball = self.ball
        ball.move(dt)

        width, height = self.framebuffer.get_size()
        if ball.pos[0] - ball.r <= 0:
            ball.pos[0] = ball.r
            ball.vel[0] = -ball.vel[0]
        elif ball.pos[0] + ball.r >= width:
            ball.pos[0] = width - ball.r
            ball.vel[0] = -ball.vel[0]
        if ball.pos[1] - ball.r <= 0:
            ball.pos[1] = ball.r
            ball.vel[1] = -ball.vel[1]
        elif ball.pos[1] + ball.r >= height:
            ball.pos[1] = height - ball.r
            ball.vel[1] = -ball.vel[1]
   
    def render(self):
        self.framebuffer.fill(self.clear_color)
        self.ball.draw(self.framebuffer)
        self.display.flip()

if __name__ == '__main__':
    game = Demo()
    game.start()
