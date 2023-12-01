
with open('input.txt') as ifile:
    COMMANDS = ifile.read().splitlines()

class Tree():
    def __init__(self, name='root', children=None, parent=None, size=0):
        self.name=name
        self.children=[]
        self.parent=parent
        self.size=size

        if children !=None:
            [self.add_child(child) for child in children]

    def __repr__(self):
        ret =  f" node: {self.name}"
        if self.children:
            ret += f", children: {self.children}"
        return ret

    def add_child(self, child):
        if isinstance(child, Tree) and child not in self.children:
            self.children.append(child)
    
    def get_child(self, child_name):
        return [child for child in self.children if child.name == child_name][0]

    def get_size(self):
        return self.size + sum([child.get_size() for child in self.children])

    def get_sizes(self):
        if not self.children:
            return
        sizes = [ self.get_size()]
        for child in self.children:
            if child_size:= child.get_sizes():
                sizes.extend(child_size)
        return sizes

#TODO: refactor
def parse_commands(command_list: list):
    filesystem=Tree()
    current_node=filesystem
    for entry in command_list:
        if entry.split(' ')[0] == 'dir':
            current_node.add_child(Tree(name=entry.split(' ')[-1], parent=current_node))
        elif entry.split(' ')[0] == '$' and entry.split(' ')[1] == 'cd':
            if entry.split(' ')[-1] == '..':        
                current_node=current_node.parent
            else:
                current_node=current_node.get_child(entry.split(' ')[-1])
        elif entry.split(' ')[1] == 'ls':
            continue
        else:   
            current_node.add_child(Tree(name=entry.split(' ')[-1], parent=current_node, size=int(entry.split(' ')[0])))
    return filesystem


def free_space(sizes_list: list)-> int:
    return 70000000 - sizes_list[0]



TREE=parse_commands(COMMANDS[1:])
SIZES_LIST=TREE.get_sizes()


def p1(sizes_list):
    return sum([size for size in sizes_list if size < 100000])

def p2(sizes_list):
    return min([size for size in sizes_list if size+free_space(sizes_list)>30000000])

print(p1(SIZES_LIST))
print(p2(SIZES_LIST))


