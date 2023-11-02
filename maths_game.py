import random
import time
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime



def generate_question_1(start, end):
    num1 = random.randint(start, end)
    num2 = random.randint(start, end)
    question = f"What is {num1} x {num2}? "
    answer = num1 * num2
    return question, answer

def multiplication_table(student_name):
    start_number = int(input("Enter the start number: "))
    end_number = int(input("Enter the end number: "))
    num_questions = int(input("Enter the number of questions: "))

    response_times = {}
    correctness = {}

    for question_number in range(1, num_questions + 1):
        question, answer = generate_question_1(start_number, end_number)
        print(f"Question {question_number}: {question}")
        
        start_time = time.time()
        user_answer = int(input("Your answer: "))
        end_time = time.time()

        response_time = round(end_time - start_time,2)

        if user_answer == answer:
            print("Correct!\n")
            correctness[question_number] = "Correct"
        else:
            print(f"Wrong! The correct answer is {answer}\n")
            correctness[question_number] = "Wrong"

        response_times[question_number] = response_time

    print("Response Times:")
    for question_number, time_taken in response_times.items():
        print(f"Question {question_number}: {time_taken:.2f} seconds")

    print("Correctness:")
    for question_number, result in correctness.items():
        print(f"Question {question_number}: {result}")
    
    timestmp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"result_mult_upto25_{timestmp}.pdf"
    generate_report(student_name, 'Multiplication Table upto 25 times', response_times, correctness, output_file)

def generate_question_2(start, end):
    num1 = random.randint(start, end)
    num2 = random.randint(1, 10)
    question = f"What is {num1} x {num2}? "
    answer = num1 * num2
    return question, answer

def multiplication_till_ten(student_name):
    start_number = int(input("Enter the start number: "))
    end_number = int(input("Enter the end number: "))
    num_questions = int(input("Enter the number of questions: "))

    response_times = {}
    correctness = {}

    for question_number in range(1, num_questions + 1):
        question, answer = generate_question_2(start_number, end_number)
        print(f"Question {question_number}: {question}")
        
        start_time = time.time()
        user_answer = int(input("Your answer: "))
        end_time = time.time()

        response_time = round(end_time - start_time,2)

        if user_answer == answer:
            print("Correct!\n")
            correctness[question_number] = "Correct"
        else:
            print(f"Wrong! The correct answer is {answer}\n")
            correctness[question_number] = "Wrong"

        response_times[question_number] = response_time

    print("Response Times:")
    for question_number, time_taken in response_times.items():
        print(f"Question {question_number}: {time_taken:.2f} seconds")

    print("Correctness:")
    for question_number, result in correctness.items():
        print(f"Question {question_number}: {result}")

    timestmp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"result_mult_upto10_{timestmp}.pdf"
    generate_report(student_name, 'Multiplication Table upto 10 times', response_times, correctness, output_file)


def generate_question_3(digit1, digit2):
    num1 = random.randint(10 ** (digit1 - 1), 10 ** digit1 - 1)
    num2 = random.randint(10 ** (digit2 - 1), 10 ** digit2 - 1)
    question = f"What is {num1} x {num2}? "
    answer = num1 * num2
    return question, answer

def different_digit_types(student_name):
    digit1 = int(input("Enter the number of digits for the first number: "))
    digit2 = int(input("Enter the number of digits for the second number: "))
    num_questions = int(input("Enter the number of questions: "))

    response_times = {}
    correctness = {}

    for question_number in range(1, num_questions + 1):
        question, answer = generate_question_3(digit1, digit2)
        print(f"Question {question_number}: {question}")
        
        start_time = time.time()
        user_answer = int(input("Your answer: "))
        end_time = time.time()

        response_time = round(end_time - start_time,2)

        if user_answer == answer:
            print("Correct!\n")
            correctness[question_number] = "Correct"
        else:
            print(f"Wrong! The correct answer is {answer}\n")
            correctness[question_number] = "Wrong"

        response_times[question_number] = response_time

    print("Response Times:")
    for question_number, time_taken in response_times.items():
        print(f"Question {question_number}: {time_taken:.2f} seconds")

    print("Correctness:")
    for question_number, result in correctness.items():
        print(f"Question {question_number}: {result}")

    timestmp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"result_mult_advance_{timestmp}.pdf"
    generate_report(student_name, 'Advance Multiplication of different digits', response_times, correctness, output_file)


def generate_question_4(digit1, digit2):
    divisor = random.randint(10 ** (digit1 - 1), 10 ** digit1 - 1)
    dividend = divisor * random.randint(1, 10 ** digit2 // divisor)
    answer = dividend // divisor
    question = f"What is {dividend} / {divisor}? "
    return question, answer

def division_table(student_name):
    digit1 = int(input("Enter the number of digits for the divisor: "))
    digit2 = int(input("Enter the number of digits for the dividend: "))
    num_questions = int(input("Enter the number of questions: "))

    response_times = {}
    correctness = {}

    for question_number in range(1, num_questions + 1):
        question, answer = generate_question_4(digit1, digit2)
        print(f"Question {question_number}: {question}")
        
        start_time = time.time()
        user_answer = int(input("Your answer: "))
        end_time = time.time()

        response_time = round(end_time - start_time,2)

        if user_answer == answer:
            print("Correct!\n")
            correctness[question_number] = "Correct"
        else:
            print(f"Wrong! The correct answer is {answer}\n")
            correctness[question_number] = "Wrong"

        response_times[question_number] = response_time

    print("Response Times:")
    for question_number, time_taken in response_times.items():
        print(f"Question {question_number}: {time_taken:.2f} seconds")

    print("Correctness:")
    for question_number, result in correctness.items():
        print(f"Question {question_number}: {result}")

    timestmp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"result_division_simple_{timestmp}.pdf"
    generate_report(student_name, 'Division with zero reminder', response_times, correctness, output_file)


def generate_question_5(digit1, digit2):
    divisor = round(random.uniform(10 ** (digit1 - 1), 10 ** digit1 - 1), 2)
    dividend = round(random.uniform(10 ** (digit2 - 1), 10 ** digit2 - 1), 2)
    answer = round(dividend / divisor, 2)
    question = f"What is {dividend} / {divisor}? "
    return question, answer

def division_of_decimal(student_name):
    digit1 = int(input("Enter the number of digits for the divisor: "))
    digit2 = int(input("Enter the number of digits for the dividend: "))
    num_questions = int(input("Enter the number of questions: "))

    response_times = {}
    correctness = {}

    for question_number in range(1, num_questions + 1):
        question, answer = generate_question_5(digit1, digit2)
        print(f"Question {question_number}: {question}")
        
        start_time = time.time()
        #user_answer = round(float(input("Your answer up to 2 decimal points: "), 2))
        user_answer = round(float(input("Your answer up to 2 decimal points: ")),2) 
        end_time = time.time()

        response_time = round(end_time - start_time,2)

        if user_answer == answer:
            print("Correct!\n")
            correctness[question_number] = "Correct"
        else:
            print(f"Wrong! The correct answer is {answer}\n")
            correctness[question_number] = "Wrong"

        response_times[question_number] = response_time

    print("Response Times:")
    for question_number, time_taken in response_times.items():
        print(f"Question {question_number}: {time_taken:.2f} seconds")

    print("Correctness:")
    for question_number, result in correctness.items():
        print(f"Question {question_number}: {result}")

    timestmp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"result_Division_complex_{timestmp}.pdf"
    generate_report(student_name, 'Complex Decimal Division', response_times, correctness, output_file)


def generate_question_6(digit1, digit2):
    divisor = random.randint(-10 ** (digit1 - 1), 10 ** (digit1 - 1))
    dividend = random.randint(-10 ** (digit2 - 1), 10 ** (digit2 - 1))
    
    # Ensure that divisor is not zero
    while divisor == 0:
        divisor = random.randint(-10 ** (digit1 - 1), 10 ** (digit1 - 1))
    
    answer = round(dividend / divisor, 2)
    question = f"What is {dividend} / {divisor}? "
    return question, answer

def division_decimal_integer_input(student_name):
    digit1 = int(input("Enter the number of digits for the divisor: "))
    digit2 = int(input("Enter the number of digits for the dividend: "))
    num_questions = int(input("Enter the number of questions: "))

    response_times = {}
    correctness = {}

    for question_number in range(1, num_questions + 1):
        question, answer = generate_question_6(digit1, digit2)
        print(f"Question {question_number}: {question}")
        
        start_time = time.time()
        user_answer = round(float(input("Your answer up to 2 decimal points: ")), 2)
        end_time = time.time()

        response_time = round(end_time - start_time,2)

        if user_answer == answer:
            print("Correct!\n")
            correctness[question_number] = "Correct"
        else:
            print(f"Wrong! The correct answer is {answer}\n")
            correctness[question_number] = "Wrong"

        response_times[question_number] = response_time

    print("Response Times:")
    for question_number, time_taken in response_times.items():
        print(f"Question {question_number}: {time_taken:.2f} seconds")

    print("Correctness:")
    for question_number, result in correctness.items():
        print(f"Question {question_number}: {result}")

    timestmp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"result_Division_Semi_complex_{timestmp}.pdf"
    generate_report(student_name, 'Semi Complex Decimal Division', response_times, correctness, output_file)


def generate_report(student_name, subject_name, time_dict, correctness_dict, output_file):
    # Check if the dictionaries have the same keys
    if set(time_dict.keys()) != set(correctness_dict.keys()):
        raise ValueError("Input dictionaries do not have the same keys.")

    # Create a list of lists for the table data
    table_data = [["Question", "Time", "Correctness"]]

    for question, time in time_dict.items():
        correctness = correctness_dict[question]
        table_data.append([question, time, correctness])

    # Create the PDF
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    elements = []

    # Create the header content
    header_content = [
        Paragraph(f"Student Name: {student_name}", getSampleStyleSheet()['Normal']),
        Paragraph(f"Subject Name: {subject_name}", getSampleStyleSheet()['Normal']),
        Paragraph(f"Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", getSampleStyleSheet()['Normal']),
    ]

    # Create the header
    header = Table([header_content], colWidths='*')
    header.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ]))
    elements.append(header)

    # Create the table
    table = Table(table_data, colWidths=[200, 80, 80])
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)

# # Example usage:
# student_name = "John Doe"
# subject_name = "Math"
# time_dict = {
#     "Question 1": "10:30",
#     "Question 2": "11:15",
#     "Question 3": "12:00",
# }
# correctness_dict = {
#     "Question 1": "Correct",
#     "Question 2": "Incorrect",
#     "Question 3": "Correct",
# }

# generate_report(student_name, subject_name, time_dict, correctness_dict, "output_result.pdf")



