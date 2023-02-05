import sys


class Node:
    def __init__(self, name, dir=False, size=0, children=[], parent=None):
        self.name = name
        self.dir = dir
        self.size = size
        self.children = children
        self.parent = parent

    def __str__(self):
        if self.dir:
            return f"{self.name} ({self.size}) -> {len(self.children)}"

        return f"{self.name} ({self.size})"


def parse_tree(lines):
    root = Node("/", dir=True)

    cwd = root
    for line in lines:
        if line[0] == "$":
            if line[2:4] == "ls":
                continue
            if line[2:4] == "cd":
                target = line[5:].replace("\n", "")
                if target == "/":
                    cwd = root
                    continue
                if target == "..":
                    cwd = cwd.parent
                    continue

                # find matching child if exists
                matches = list(filter(
                    lambda chld: chld.name == target, cwd.children))

                # dir already exists
                if len(matches) > 0:
                    cwd = matches[0]
                    continue

                # create new dir node and change to it
                new_dir = Node(target, dir=True, parent=cwd, children=[])
                cwd = new_dir

        # line stands for dir content
        info, name = line.replace('\n', '').split(' ')

        # create dir node
        if info == 'dir':
            dir = Node(name, dir=True, parent=cwd, children=[])
            cwd.children.append(dir)
            continue

        # create file node
        file = Node(name, size=int(info), parent=cwd, children=[])
        cwd.children.append(file)

    return root


def print_tree(directory_tree, depth=0):
    print(f"{depth*2*' '}{directory_tree}")
    for child in directory_tree.children:
        print_tree(child, depth=depth+1)


def calculate_dir_sizes(directory_tree):
    # for files only return size
    if directory_tree.dir:
        # recursive call for all children
        for child in directory_tree.children:
            calculate_dir_sizes(child)
        # set own size to sum of children (files and dirs)
        directory_tree.size = sum(
            map(lambda child: child.size, directory_tree.children))


def sum_smaller_dirs(directory_tree, threshold):
    sum = 0
    if directory_tree.dir:
        if directory_tree.size <= threshold:
            sum += directory_tree.size
        for child in directory_tree.children:
            sum += sum_smaller_dirs(child, threshold)

    return sum


def calculate_dirs(lines):
    directory_tree = parse_tree(lines)

    calculate_dir_sizes(directory_tree)
    # print_tree(directory_tree)

    return sum_smaller_dirs(directory_tree, 100000)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_dirs(lines))
