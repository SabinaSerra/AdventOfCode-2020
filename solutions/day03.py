import utils as utils

def is_tree(block:str):
    return block == "#"

def count_trees(tree_map: list, currPos: tuple[int, int], strategy: tuple[int, int]):
    if currPos[1] >= len(tree_map):
        return 0
    if is_tree(tree_map[currPos[1]][currPos[0]]):
        counter = 1 
    else:
        counter = 0 
    new_x = (currPos[0]+ strategy[0]) % len(tree_map[0])
    new_y = currPos[1] + strategy[1]
    return counter + count_trees(tree_map, (new_x, new_y), strategy)

def part1(tree_map: list):
    return count_trees(tree_map, (0,0), (3,1))

def part2(tree_map: list):
    strategies = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    startPos = (0,0)
    counter = 1
    for strategy in strategies:   
        counter *= count_trees(tree_map, startPos, strategy)
    return counter

def main():
    tree_map, part = utils.init() 
    if part == 1:
        res = part1(tree_map)
    else:
        res = part2(tree_map)
    print(res)

if __name__ == "__main__":
    main()