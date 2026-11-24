
import pygame
from fly_in import ParseError, MapGen, Map, MapError, fly_in, Drone

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

def main():
	path = "maps/challenger/01_the_impossible_dream.txt"
	try:
		#pygame.init()
		#screen = pygame.display.set_mode((800, 600))
		running = True
		mymap = MapGen(path).parser()
		mymap.create_drones()
		fly_in(mymap.drones)
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
	except ParseError as e:
		print(f"{e}")
	except MapError as e:
		print(f"{e}")
	except ValueError as e:
		print(f"{e}")
	except FileNotFoundError as e:
		print(f"{e}")


if __name__ == "__main__":
	main()