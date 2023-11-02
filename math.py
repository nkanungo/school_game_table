from maths_game import multiplication_table, multiplication_till_ten, different_digit_types, division_table, division_of_decimal, division_decimal_integer_input
def main():
    print('Welcome to the mathematics game')
    print('It has 6 different types of games. Choose the one you want to play with the options.')

    student_name = input('Enter Your name, which will be printed in the report: ')

    while True:
        prn = '''Choose the Option to start playing:
        1. Multiplication (Both Multiplier and Multiplicand up to 25)
        2. Multiplication (Multiplier up to 25 and Multiplicand up to 10)
        3. Multiplication (Of different digits)
        4. Division (Simple perfect division)
        5. Division (Complex division in which Dividend and Divisor can both be decimals and so can the answer)
        6. Division (A little complex division in which Dividend and Divisor are Integers, but the answer can be a decimal)

        For division problems, please answer up to 2 decimal points
        '''

        print(prn)

        choice = input('Choose an option (1/2/3/4/5/6): ')

        if choice == '1':
            multiplication_table(student_name)
            break
        elif choice == '2':
            multiplication_till_ten(student_name)
            break
        elif choice == '3':
            different_digit_types(student_name)
            break
        elif choice == '4':
            division_table(student_name)
            break
        elif choice == '5':
            division_of_decimal(student_name)
            break
        elif choice == '6':
            division_decimal_integer_input(student_name)
            break
        else:
            print('Invalid option. Please choose 1, 2, 3, 4, 5, or 6.')

if __name__ == "__main__":
    main()
