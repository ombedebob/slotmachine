
import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
    }

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
    }

#check winnings
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings,winning_lines

#get spin
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns =[]
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

#print slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1 :
                print(column[row], end=" | ")
            else:
                print(column[row],end="")

        print()

#get the amount player would like to deposit
def deposit():
    while True:
        amount = input('How much would you like to enter? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Enter amount greater than zero please!')
        else:
            print('Enter a number!')

    return amount

#get number of lines player would like to bet on
def get_number_of_lines():
    while True:
        lines = input(f'How many lines would you like to bet on? 1-{str(MAX_LINES)}: ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter valid number of lines!')
        else:
            print('Enter a number!')

    return lines

#get the amount player would like to bet on each line
def get_bet():
    while True:
        amount = input('How much would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print('Enter amount greater than zero please!')
        else:
            print('Enter a number!')

    return amount

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'You do not have enough to make this bet. Your balance us: {balance}')
        else:
            break

    print(f'You are betting ${bet} on {lines} lines. Your total bet equals {total_bet}')

    slots = get_slot_machine_spin(COLS,ROWS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f'You won ${winnings}')
    print(f'You won on lines: ',*winning_lines)
    return winnings - total_bet

#main program
def main():
    balance = deposit()
    while True:
        print(f'current balance is ${balance}')
        answer = input('Press enter to play (q to quit)')
        if answer == 'q':
            break
        else:
            balance += spin(balance)

    print(f'Your balance is ${balance}')

main()