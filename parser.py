# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smeza-ro <smeza-ro@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/14 11:09:29 by smeza-ro          #+#    #+#              #
#    Updated: 2026/10/14 12:14:48 by smeza-ro         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class

class MapGen():
    def __init__(self, path):
        self.path = path
        self.nb = nb

    def
    def parser(self):
        with open(path, "r") as f:
            for i, line in enumerate(f):
                if i == 1:
                    self.nb = line
                    line.startswith("nb_drones")
                        