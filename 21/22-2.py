# Advent of Code 2022 - Puzzle 21-2
import math

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line)

class Monkey:
    def __init__(self, name, mnktype):
        self.name = name
        self.mnktype = mnktype
        self.HasValue = False
        self.IsSolved = False
        
    def setValue(self, value):
        self.value = value
        self.HasValue = True

    def setEquation(self, mnk1, mnk2, operator):
        self.mnk1 = mnk1
        self.mnk2 = mnk2
        self.operator = operator

riddle_guessed = False
riddle_solved = False

# Seed with vaguely accurate order of magnitude with a guess confirmed to be too low
guess = 100000000000
guessfactor = 10000000000
last_guess_low = True


# Repeat the solving of part 1, starting with 'guess' as value for humn, and increasing/decreasing the value of guess every loop depending on whether
# the guess is too low or too high. Start with a big increment then divide by ten every time the result flips from too high to too low or vice versa.
# This exponentially narrows down the search space for each flip. 
# Could skip the solving of part 1 in the loop by extracting the mathematical equation from the list of monkeys to solve for humn, but this method
# is fast enough not to need to
while(not riddle_guessed):

    monkeys = []
    solvedmonkeys = dict({})

    # Create monkeys
    for line in puzzleinput:
        if '+' in line or '-' in line or '/' in line or '*' in line:
            mnk_name = line[:4]
            mnk1 = line[6:10]
            mnk2 = line[13:17]
            operator = line[11]
            tmp_mnk = Monkey(mnk_name, "Equation")
            tmp_mnk.setEquation(mnk1=mnk1,mnk2=mnk2,operator=operator)
            monkeys.append(tmp_mnk)
        else:
            line = line.replace(':','').split(' ')
            tmp_mnk = Monkey(line[0],"Number")
            tmp_mnk.setValue(line[1])
            monkeys.append(tmp_mnk)
            solvedmonkeys[tmp_mnk.name] = tmp_mnk.value

    solvedmonkeys['humn'] = guess

    riddle_solved = False

    while(not riddle_solved):
    
        for monkey in monkeys:
            if monkey.mnktype == "Equation" and monkey.IsSolved == False:
                if monkey.mnk1 in solvedmonkeys and monkey.mnk2 in solvedmonkeys:
                    monkey.mnk1 = solvedmonkeys[monkey.mnk1]
                    monkey.mnk2 = solvedmonkeys[monkey.mnk2]

                    if monkey.operator == '+':
                        monkey.setValue(int(monkey.mnk1) + int(monkey.mnk2))
                    elif monkey.operator == '-':
                        monkey.setValue(int(monkey.mnk1) - int(monkey.mnk2))
                    elif monkey.operator == '*':
                        monkey.setValue(int(monkey.mnk1) * int(monkey.mnk2))
                    elif monkey.operator == '/':
                        monkey.setValue(int(int(monkey.mnk1) / int(monkey.mnk2)))
                    else:
                        print("Error with operator")
                    
                    monkey.IsSolved = True
                    solvedmonkeys[monkey.name] = monkey.value
                    
                    if monkey.name == 'root':
                        print("root:", monkey.mnk1, "=", monkey.mnk2)
                        if(monkey.mnk1 > monkey.mnk2):
                            if last_guess_low:
                                guess += guessfactor
                                print("Guess is too low - increasing guess to ", guess)
                                riddle_solved = True
                            else:
                                if guessfactor > 1:
                                    guessfactor = guessfactor // 10
                                    print("Guess factor reduced to",guessfactor)
                                guess += guessfactor
                                print("Guess is too low - increasing guess to ", guess)
                                last_guess_low = True
                                riddle_solved = True
                        elif(monkey.mnk1 < monkey.mnk2):
                            if not last_guess_low:
                                guess -= guessfactor
                                print("Guess is too high - decreasing guess to ", guess)
                                riddle_solved = True
                            else:
                                if guessfactor > 1:
                                    guessfactor = guessfactor // 10
                                    print("Guess factor reduced to",guessfactor)
                                guess -= guessfactor
                                print("Guess is too high - decreasing guess to ", guess)
                                riddle_solved = True
                                last_guess_low = False
                        else:
                            print("Success - correct value for humn is",guess)
                            riddle_solved = True
                            riddle_guessed = True
