def division(n1,n2):
    """
    divide numbers.
    :param n1: first number to calculate
    :param n2: second number to calculate
    :return: result of division
    """
    return n1 / n2

dictionary={"+":add, "-":subtraction, "*":multiplication, "/":division}


question="no"
result=0
while True:

    number_f=0
    if question=="no":
        number_f=int(input("type your first number: "))
    else:
        number_f=result


    mathematical_operator=input("type the choice: ")
    number_s=int(input("type your second number: "))
    result=dictionary[mathematical_operator](number_f,number_s)
    print(dictionary[mathematical_operator](number_f,number_s))

    question=input("do you want to continue the thing? yes or no :  ")

#
# import art
#
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }
#
# # print(operations["*"](4, 8))
#
#
# def calculator():
#     print(art.logo)
#     should_accumulate = True
#     num1 = float(input("What is the first number?: "))
#
#     while should_accumulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What is the next number?: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
#
#         if choice == "y":
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator()
#
#
# calculator()