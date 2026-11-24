# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smeza-ro <smeza-ro@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/14 11:05:12 by smeza-ro          #+#    #+#              #
#    Updated: 2026/10/14 11:08:45 by smeza-ro         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from fly_in import ParseError, MapGen, Map, MapError, fly_in, Drone

def main():
	path = "maps/medium/03_priority_puzzle.txt"
	try:
		mymap = MapGen(path).parser()
		mymap.create_drones()
		fly_in(mymap.drones)
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