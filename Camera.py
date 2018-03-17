import pygame, sys
import pygame.camera


class Button(pygame.sprite.Sprite):
	def __init__(self):
		super(Button, self).__init__()
		self.surf = pygame.Surface((40,40))
		self.surf.fill((255,255,255))
		self.rect = self.surf.get_rect()
	def click(self):
		pos_x, pos_y = pygame.mouse.get_pos()
		print(pos_x, pos_y)




class Camera(Button):
	"""docstring for Camera"""
	def __init__(self):
		super (Camera, self).__init__()
		pygame.init()
		self.screen  = pygame.display.set_mode((800, 600), 0, 32)
		pygame.display.set_caption("Camera")
		pygame.camera.init()
		self.size = (640, 480)
		self.cam = pygame.camera.Camera("/dev/video0", self.size)
		self.cam.start()
		self.img = pygame.Surface(self.size, 0, self.screen)
	def get_images(self):
		if self.cam.query_image():
			self.img = self.cam.get_image()
		self.screen.blit(self.img, ((800 - self.size[0]) / 2, 0))
		pygame.display.flip() 
	
	def main(self):
		mainloop = True
		while mainloop:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					mainloop = False
					self.cam.stop()
			self.screen.fill((0,0,0))
			self.screen.blit(self.surf, self.rect)
			self.get_images()
		pygame.quit()


if __name__ == "__main__":
	cam = Camera()
	cam.main()