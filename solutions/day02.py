import utils as utils

def get_letter(password: str, ind: int):
    try:
        letter = password[ind]
    except:
        letter = "" 
    return letter

def part2(password_inputs: list):
    valid_counter = 0
    for password_input in password_inputs:
        amount, letter, password = password_input.split(" ")
        inds = [(int(num) - 1) for num in amount.split("-")]
        letter = letter[:-1]
        letters_at_inds = [get_letter(password, ind) for ind in inds]
        if letters_at_inds.count(letter) == 1:
            valid_counter +=1
    return valid_counter

def part1(password_inputs: list):
    valid_counter = 0
    for password_input in password_inputs:
        amount, letter, password = password_input.split(" ")
        min_amount, max_amount = [int(num) for num in amount.split("-")]
        letter = letter[:-1]
        if (min_amount <= password.count(letter) <= max_amount):
            valid_counter += 1

    return valid_counter

def main():
    passwords, part = utils.init()
    if part == 1:
        res = part1(passwords)
    else:
        res = part2(passwords)
    print(res)

if __name__ == "__main__":
    main()
