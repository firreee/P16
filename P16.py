def calculate_sum(n):
    if n <= 0:
        raise ValueError("Number cannot be negative")
    elif n == 1:
        return 1
    else:
        return n + calculate_sum(n - 1)

def main():
    print("--- sum up numbers ---")
    another_number = 'y'
    while another_number.lower() == 'y':
        try:
            num = int(input("Enter a number: "))
            if num <= 0:
                print("Number cannot be negative")
            else:
                result = calculate_sum(num)
                print(f"{'+'.join(map(str, range(num, 0, -1)))} = {result}")
        except ValueError:
            print("Invalid input detected. Please enter a valid integer.")

        another_number = input("Another number (y/n): ").strip()

    print("--- done ---")

main()
