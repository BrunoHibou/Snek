import pygame
import random

# Definição de cores
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definição de constantes
SCREEN_WIDTH =  600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 10
FPS = 15

# Inicialização do Pygame
pygame.init()

# Criação da janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cobrinha')

# Classe da cobrinha
class Snake:
    def __init__(self, screen):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.dx = BLOCK_SIZE
        self.dy = 0
        self.length = 1
        self.body = [(self.x, self.y)]
        self.counter = 0
        self.color = GREEN
        self.screen_fill = BLACK

    # Método para mover a cobrinha
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            del self.body[0]

    # Método para desenhar a cobrinha
    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, self.color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

    # Método para checar colisão com a parede
    def check_wall_collision(self):
        if self.x < 0 or self.x >= SCREEN_WIDTH or self.y < 0 or self.y >= SCREEN_HEIGHT:
            return True
        return False

    # Método para checar colisão com o corpo
    def check_self_collision(self):
        for x, y in self.body[:-1]:
            if self.x == x and self.y == y:
                return True
        return False

    # Método para aumentar o tamanho da cobrinha
    def eat(self):
        self.length += 1
        self.counter+= 1
        if self.counter%2 == 0:
            if self.color == BLACK:
                self.color = GREEN
                self.screen_fill = BLACK
            else:
                self.color = BLACK
                self.screen_fill = WHITE


# Classe do alimento
class Food:
    def __init__(self):
        self.x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
        self.y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)

    # Método para desenhar o alimento
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    # Método para checar colisão com a cobrinha
    def check_collision(self, snake):
        if self.x == snake.x and self.y == snake.y:
            return True
        return False

# Criação da cobrinha e do alimento
snake = Snake(screen)
food = Food()

# Criação do objeto de relógio do Pygame
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    has_moved = False
    # Manipulação de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Controles da cobrinha com as setas do teclado
        if event.type == pygame.KEYDOWN and has_moved == False:
            if event.key == pygame.K_LEFT and snake.dx == 0:        
                snake.dx = -BLOCK_SIZE
                snake.dy = 0
                has_moved = True
            elif event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = BLOCK_SIZE
                snake.dy = 0
                has_moved = True
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dy = -BLOCK_SIZE
                snake.dx = 0
                has_moved = True
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dy = BLOCK_SIZE
                snake.dx = 0
                has_moved = True

# Movimento da cobrinha

    snake.move()
    
    # Checagem de colisões
    if snake.check_wall_collision() or snake.check_self_collision():
        pygame.quit()
        quit()
    if food.check_collision(snake):
        snake.eat()
        food = Food()

    # Desenho dos objetos na tela
    screen.fill(snake.screen_fill)
    snake.draw()
    food.draw()
    pygame.display.update()

    # Controle de FPS
    clock.tick(FPS)

			
               
