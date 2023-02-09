from functools import reduce
import operator

with open("inputs/input11.txt") as ifile:
    inp = [monkey.split("\n") for monkey in ifile.read().split("\n\n")]


class Monkey():
    ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
}
    def __init__(self, monkey_index: int, items: list, operation: str, operand, test_number: int, target_monkeys: tuple):
        self.monkey_index = monkey_index
        self.items = items
        self.operation = operation
        self.operand = operand
        self.test_number = test_number
        self.target_monkeys = target_monkeys
        self.inspected = 0 
    
    def __repr__(self) -> str:
        return f"""
        Monkey {self.monkey_index}
        items: {self.items}
        Operation: new = old {self.operation} {self.operand}
        Test: divisible by {self.test_number}
            If true: throw to monkey {self.target_monkeys[0]}
            If false: throw to monkey {self.target_monkeys[1]}
        """

    def test(self, num: int):
        return num % self.test_number == 0

    def operate(self, num: int)-> int:
        if self.operand == 'old':
            return int(self.ops[self.operation](num, num))
        return int(self.ops[self.operation](num, int(self.operand)))

    def inspect_items(self, test_product: int, part_one = True)-> dict:
        passes = {}   # {monkey: item}  pass item to monkey
        for idx, item in enumerate(list(self.items)): # list() is used to iterate over a copy of self.items
            worry_level = self.operate(item) % test_product #// 3
            if part_one:
                worry_level = worry_level // 3
            if self.test(worry_level):
                passes.setdefault(self.target_monkeys[0], []).append(worry_level)
            else:
                passes.setdefault(self.target_monkeys[1], []).append(worry_level)
            self.inspected += 1
            self.items.remove(item)
        return passes



def monkey_parser(input_monkey: list)-> Monkey:
    return Monkey(
        monkey_index=int(input_monkey[0].split()[1].strip(':')),
        items=[int(item.strip(",")) for item in input_monkey[1].split()[2:]],
        operation=input_monkey[2].split()[4],
        operand=input_monkey[2].split()[5],
        test_number=int(input_monkey[3].split()[-1]),
        target_monkeys=(int(input_monkey[4].split()[-1]),int(input_monkey[5].split()[-1])) 
    )


def create_monkey_list(input_monkeys: list)-> list[Monkey]:
    return [monkey_parser(monkey) for monkey in input_monkeys]


class MonkeyList():
    def __init__(self, monkeys: list[Monkey]) -> None:
        self.monkeys = monkeys

    def throw_item(self, monkey_index: int, items: list):
        self.monkeys[monkey_index].items.extend(items)

    def calculate_round(self, part_one = True):
        for monkey in self.monkeys:
            to_throw = monkey.inspect_items(reduce(lambda x, y: x*y, [monkey.test_number for monkey in self.monkeys]), part_one)
            for k, v in to_throw.items():
                self.throw_item(k, v)

    def get_counts(self):
        return [monkey.inspected for monkey in self.monkeys]


def compute_monkey_business(input_monkeys, part_one=True):
    rounds = 10000 if not part_one else 20 
    my_monkey_list = MonkeyList(create_monkey_list(input_monkeys))
    [my_monkey_list.calculate_round(part_one) for i in range(rounds)]
    return reduce(lambda x, y: x*y, sorted(my_monkey_list.get_counts())[-2:])


print(compute_monkey_business(inp, True))


print(compute_monkey_business(inp, False))



    

    


