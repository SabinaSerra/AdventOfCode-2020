import os
import argparse
import time 
import utils as utils

def part1(numbers: list):
    while (len(numbers) > 2):
        res = numbers[0] + numbers[-1]
        if res == 2020:
            return [numbers[0], numbers[-1]]
        if res > 2020: 
            numbers.pop(-1)
        if res < 2020:
            numbers.pop(0)
    return numbers

def part2(numbers: list):   
    while (len(numbers) > 3):
        n0, n1, n2 = numbers[0], numbers[1], numbers[-1]
        res = n0 + n1 + n2 
        goalsum = 2020 
        if res == goalsum:
            return [n0, n1, n2]
        elif res > goalsum:
            numbers.pop(-1)
        else:
            third_num = binary_search(goalsum - (n0 + n2), numbers)
            if third_num != -1:
                return [n0, third_num, n2]
            else:
                numbers.pop(0)
    return numbers

def binary_search(number: int, numbers: list):
    if len(numbers) == 0:
        return -1
    mid = len(numbers)//2
    mid_num = numbers[mid]
    if number == mid_num:
        return mid_num
    if number < mid_num:
        return binary_search(number, numbers[:mid])
    else:
        return binary_search(number, numbers[mid+1:])

def main():
    numbers, part = utils.init(input_type="int")
    numbers.sort()
    if part == 1:
        num1, num2 = part1(numbers)
        print(f"{num1} x {num2} = {num1 * num2}")
    else:
        num1, num2, num3 = part2(numbers)
        print(f"{num1} x {num2} x {num3} = {num1 * num2 * num3}")
    

if __name__ == "__main__":
    main()