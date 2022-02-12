##
## EPITECH PROJECT, 2021
## Makefile
## File description:
## Gomoku
##

SRC	=	src/main.cpp \
		src/Core.cpp \

OBJ		=	$(SRC:.cpp=.o)

NAME	=	jeu

RM		+=	-r

CC		=	g++ -std=c++17 -lsfml-graphics -lsfml-window -lsfml-system

CFLAGS		+=	 -Wall -Wextra

CPPFLAGS	+=	-I include/

LDFLAGS		+=

.PHONY:	all clean fclean re

all:	$(NAME)

$(NAME):	$(OBJ)
	$(CC) $(CFLAGS) -o $(NAME) $(OBJ) $(LDFLAGS)

clean:
	$(RM) $(OBJ)
	$(RM) *.o
	$(RM) *~
	$(RM) */*~
	$(RM) *.gc*
	$(RM) vgcore.*

fclean: clean
	$(RM) $(NAME)

re:	fclean all
