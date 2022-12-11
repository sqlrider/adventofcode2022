# Advent of Code 2022 - Puzzle 11-2

import math

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        puzzleinput.append(line.strip('\n').replace(',','').split(' '))

num_monkeys = int((len(puzzleinput) + 1) / 7)

class monkey:
    divisor = 0
    true_throw_to_monkey = 0
    false_throw_to_monkey = 0
    operator = ''
    operand = ''
    items_inspected = 0

    def __init__(self, p_divisor, p_true_throw_to_monkey, p_false_throw_to_monkey, p_operator, p_operand):
        self.divisor = p_divisor
        self.true_throw_to_monkey = p_true_throw_to_monkey
        self.false_throw_to_monkey = p_false_throw_to_monkey
        self.operator = p_operator
        self.operand = p_operand
        self.items = []

    def addItem(self, p_item):
        self.items.append(p_item)

    def clearItems(self):
        self.items = []

    def printItems(self):
        print("Items:",self.items)
        

monkeys = []
product_of_divisors = 1

for a in range(0,num_monkeys):

    divisor = int(puzzleinput[a * 7 + 3][5])
    true_throw_to_monkey = int(puzzleinput[a * 7 + 4][9])
    false_throw_to_monkey = int(puzzleinput[a * 7 + 5][9])
    operator = puzzleinput[a * 7 + 2][6]
    operand = puzzleinput[a * 7 + 2][7]

    new_monkey = monkey(divisor, true_throw_to_monkey,false_throw_to_monkey,operator,operand)

    for item in puzzleinput[a * 7 + 1][4:]:
        new_monkey.addItem(int(item))

    monkeys.append(new_monkey)

    #Part 2, see later comment
    product_of_divisors *= divisor

for i in range(0,10000):

    #print("Round",i)
    a = 0
    for mnk in monkeys:

        for item in mnk.items:
            # Monkey inspects item
            if mnk.operator == '*':
                if mnk.operand == 'old':
                    item = item * item
                elif mnk.operand.isdigit():
                    item = item * int(mnk.operand)
                else:
                    print("ERROR")

            elif mnk.operator == '+':
                if mnk.operand == 'old':
                    item = item + item
                elif mnk.operand.isdigit():
                    item = item + int(mnk.operand)
                else:
                    print("ERROR")

            mnk.items_inspected += 1

            # Monkey no longer gets bored in part 2, so can't / by 3
            # But this results in monstrous levels that cannot be computed.
            # So need to reduce the number somehow, but in a way that *doesn't affect this or the other monkeys' tests for modulo*.
            # Given that tests are all modulo, use property (a mod b) mod b = a mod b and mod the result by LCM/product of all the divisors
            item = item % product_of_divisors

            # Is divisible?
            if item % mnk.divisor == 0:
                monkeys[mnk.true_throw_to_monkey].addItem(item)
            else:
                monkeys[mnk.false_throw_to_monkey].addItem(item)

        # Clear current monkey's list of items
        mnk.clearItems()
        a += 1

# Check output
#for mnk in monkeys:
#    mnk.printItems()

results = []
a = 0
for mnk in monkeys:
    print("Monkey",a,"items inspected:",mnk.items_inspected)
    results.append(mnk.items_inspected)
    a += 1

results.sort(reverse=True)
print("Monkey business:",results[0] * results[1])