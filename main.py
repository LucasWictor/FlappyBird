import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# font
font = pygame.font.SysFont('Bauhaus 93', 60)

# colors
white = (255, 255, 255)

# game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

# rendering
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
    score = 0
    return score

class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range(1, 4):
			img = pygame.image.load(f'img/bird{num}.png')
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
		self.clicked = False

        def update(self):
			if flying == True:
				# gravity
				self.vel += 0.5
				if self.vel > 8:
					self.vel = 8
				if self.rect.bottom < 768:
					self.rect.y += int(self.vel)
					#jump
					if game_over == False;
					if pygame.mouse.get.pressed()[0] == 1 and self.clicked == False:
						self.clicked = True
						self.vel = -10
					if pygame.mouse.get.pressed()[0] == 0:
						self.clicked = False
						# Animation
						self.counter += 1
						flap_cooldown = 5

						if self.counter > flap_cooldown:
							self.counter = 0
							self.index += 1
							if self.index >= len(self.images):
								self.index = 0
							self.image = self.images[self.index]

							#rotate bird
						self.image = pygame.transform.rotate(self.image, self.vel * -2)
					else:
						self.image = pygame.transform.rotate(self.image, self.vel * -90)

class Pipe(pygame.sprite.Sprite):
	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/pipe.png')
		self.rect = self.image.get_rect()
		#pos 1 is the top, -1 is the the bottom
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
		if position == -1:
			self.rect.topleft = [x, y + int(pipe_gap / 2)]

			def update(self):
				self.rect.x -= scroll_speed
				if self.rect.right < 0:
					self.kill()

