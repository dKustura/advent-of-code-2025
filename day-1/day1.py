import os

def goLeft(value, step):
    return (value - step) % 100

def goRight(value, step):
    return (value + step) % 100

def day1_part1():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.readlines()
        value = 50
        count = 0

        for line in lines:
            direction = line[0]
            step = int(line[1:])

            if direction == 'L':
                value = goLeft(value, step)
            else:
                value = goRight(value, step)
                
            if value == 0:
                count += 1
        
        return count
    
def day1_part2():
    with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
        lines = f.read().splitlines()
        value = 50
        count = 0

        for line in lines:
            direction = line[0]
            step = int(line[1:])

            if direction == 'L':
                if value - step == 0:
                    count += 1
                elif value - step < 0:
                    if value != 0:
                        count += 1
                    count += (step - value) // 100
                value = goLeft(value, step)
            else:
                count += (value + step) // 100
                value = goRight(value, step)
        
        return count

part1 = day1_part1()
print("Password1: ", part1)

part2 = day1_part2()
print("Password2: ", part2)