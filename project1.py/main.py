import random
MAX_LINES = 3
MAX_BET =100
MIN_BET =1

ROWS = 3
COLS = 3
symbol_count ={
    "^":2,
    "#":4,
    "?":6,
    "$":8
}
symbol_value ={
    "^":5,
    "#":4,
    "?":3,
    "$":2
}
def check_winnings(columns,lines,bet,values):
    winnings =0
    for line in range(lines):
        winning_lines =[]
        symbol =columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet 
            winning_lines.append(line + 1)
    return winnings,winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    colums =[]
    for _ in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value =random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        colums.append(column)
    return colums
def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
              print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()    

def deposit():
    while True:
        amount = input("what would you like to deposit in $ ?:")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("enter a number")

    return amount
def get_num_of_lines():
     while True:
        lines = input("enter the number of lines to bet (1-"+str(MAX_LINES) + " ):")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("LINES must be greater than 0 less than 3")
        else:
            print("enter a number")

     return lines

def get_bet():
    while True:
        amount = input("enter the amount you want to bet on each line:$")
        if amount.isdigit():
            amount = int(amount)
            
            if MIN_BET <= amount <= MAX_BET:
                
                break
              
            else:
                print(f"your amount should be between ${MIN_BET} to ${MAX_BET}")
        else:
            print("enter a valid number:")
   
    return amount      

def spin(balance):
  lines = get_num_of_lines()
  while True:
    bet = get_bet()
   
    total_bet = bet*lines
    if total_bet>balance:
        print("you cant bet greater than your balance :(  ")
    else:
      break
  print(f"you are betting ${bet} on {lines}. total bet is {total_bet}")
  slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
  print_slot(slots)
  winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
  print(f"you won ${winnings}")
  print(f"you won on lines", *winning_lines)
  return winnings - total_bet

def main():
  balance = deposit()
  while True:
      print(f"Current balance is ${balance}")
      answer = input ("press enter to spin (q to Quit)")
      if answer == "q":
        break
      balance += spin(balance)
  print(f"you left with ${balance}")

main()