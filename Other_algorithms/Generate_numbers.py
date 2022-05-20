def generate_numbers(amplitude: int, count_digit: int, prefix = None):
    prefix = prefix or []
    if count_digit == 0:
        print(*prefix)
        return
    for digit in range(amplitude):
        prefix.append(digit)
        generate_numbers(amplitude, count_digit-1, prefix)
        prefix.pop()

generate_numbers(2, 3)