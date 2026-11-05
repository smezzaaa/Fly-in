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

from fly_in import ParseError, MapGen, Map

def main():
	path = "maps/easy/03_basic_capacity.txt"
	try:
		mymap = MapGen(path).parser()
		mymap.get_path()
		mymap.create_drones()
	except ParseError as e:
		print(f"{e}")
	except ValueError as e:
		print(f"{e}")
	except FileNotFoundError as e:
		print(f"{e}")


if __name__ == "__main__":
	main()