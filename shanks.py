import math

def check_prime(num):
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def enter_number():
    while True:
        print("Enter prime number: (0 to end) ", end="")
        num = input()
        try:
            num = int(num)
        except ValueError:
            print("Not an integer")
            continue
        if num == 0 or check_prime(num):
            return num
        else:
            print("Not a prime")

def calc_rep_digits(num):
    dividend = 1
    count = 1
    all_dividends = set([dividend])
    while True:
        dividend *= 10
        new_dividend = dividend % check_number
        if new_dividend in all_dividends:
            return count
        else:
            all_dividends.add(new_dividend)
            dividend = new_dividend
            count += 1

    
if __name__ == "__main__":
    print("Calculated number of repeating digits of prime reciprocals")
    while True:
        check_number = enter_number()
        if check_number == 0:
            break
        else:
            answer = calc_rep_digits(check_number)
            print("repeating digits: ", answer)
