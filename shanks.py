def enter_number():
    print("Enter prime number: (0 to end) ", end="")
    return int(input())

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
