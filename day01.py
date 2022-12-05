from common.inputfile import InputFile


def part1(lines):
    elves = getElves(lines)
    elves.sort(key=elfSort, reverse=True)
    return str(elves[0].calories)

def part2(lines) :
    elves = getElves(lines)
    elves.sort(key=elfSort, reverse=True)
    return str(elves[0].calories + elves[1].calories + elves[2].calories)

def getElves(lines):
    elf = Elf()
    elves = []
    for line in lines:
        if (line == ''):
            elves.append(elf)
            elf = Elf()
        else:
            elf.add_calories(line);
    return elves

def elfSort(elf):
    return elf.calories

class Elf:
    def __init__(self):
        self.calories = 0

    def add_calories(self, calories):
        self.calories += int(calories)

    def __str__(self):
        return self.calories

if __name__ == '__main__':
    # input = InputFile('input-files/day01-sample.txt')
    input = InputFile('input-files/day01.txt')
    lines = input.get_contents_by_line()
    part1 = part1(lines)
    part2 = part2(lines)
    print("part 1:" + part1)
    print("part 2:" + part2)