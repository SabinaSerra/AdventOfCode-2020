import argparse
import time

def init(input_type="str"):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', "-i", type=str, required=True, help="")
    parser.add_argument('--part', "-p", type=int, required=True, choices=[1, 2,], help="")
    args = parser.parse_args()
    txt_file = args.input
    if input_type == "int":
        return read_number_file(txt_file), args.part
    else:
        return read_str_file(txt_file), args.part


def read_number_file(txt_file: str):
    numbers = []
    with open(txt_file, "r") as read_file:
        number = read_file.readline().rstrip()
        while number: 
            numbers.append(int(number))
            number = read_file.readline()
    return numbers


def read_str_file(txt_file: str):
    inputs = []
    with open(txt_file, "r") as read_file:
        inputs = read_file.read().splitlines()
    return inputs


def measure(solution, inputs):
    start = time.time()
    res = solution(inputs)
    end = time.time()
    sol_time = end - start
    print(f"Time: {sol_time}\nResult: {res}")