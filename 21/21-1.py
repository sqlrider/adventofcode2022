# Advent of Code 2022 - Puzzle 21-1

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

riddle_solved = False

# Loop over list of monkeys setting values where possible, each loop means more monkeys can be solved until finally root is solved.
while(not riddle_solved):

    for monkey in monkeys:
        if monkey.mnktype == "Equation" and monkey.IsSolved == False:
            # Check if mnk1 and mnk2 values can be replaced
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
                    print("Solved monkey",monkey.name," - value is", monkey.value, "from", monkey.mnk1, monkey.operator, monkey.mnk2)
                    riddle_solved = True
