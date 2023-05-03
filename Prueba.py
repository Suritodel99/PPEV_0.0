# Juego de 3 en raya
import sys

# Definir el tablero
board = [' '] * 9

# Definir las posiciones ganadoras
winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Función para imprimir el tablero
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Función para realizar un movimiento
def make_move(player, position):
    board[position] = player

# Función para verificar si el juego ha terminado
def game_over():
    for pos1, pos2, pos3 in winning_positions:
        if board[pos1] == board[pos2] == board[pos3] != ' ':
            return True
    if ' ' not in board:
        return True
    return False

# Función para iniciar el juego
def play_game():
    players = ['X', 'O']
    turn = 0
    while not game_over():
        player = players[turn]
        print_board()
        position = int(input(f"Jugador {player}, elige una posición (1-9): ")) - 1
        if board[position] == ' ':
            make_move(player, position)
            turn = (turn + 1) % 2
        else:
            print('La posición ya está ocupada, elige otra.')
    print_board()
    if ' ' not in board:
        print('¡Empate!')
    else:
        print(f'¡El jugador {player} ha ganado!')

if __name__ == '__main__':
    play_game()
