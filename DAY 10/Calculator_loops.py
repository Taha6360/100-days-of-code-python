import art

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return  n1 - n2
def multiply(n1, n2):
    return  n1 * n2
def divide(n1, n2):
    return n1 / n2

dicto = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def main():
    print(art.logo)
    want_to_continue = True
    first_num = int(input("Enter the first number : "))


    while(want_to_continue):

        operation = input("+\n- \n* \n/ \n Pick an operation : ")
        second_num = int(input("Enter Second Number : "))
        answer = dicto[operation](first_num, second_num)
        print(answer)
        continue_calc = input("If you want to continue the calculations enter y or enter n ").lower()
        if continue_calc == 'y':
            first_num = answer
        else:
            print("\n"*20)
            want_to_continue = False
            main()


main()
