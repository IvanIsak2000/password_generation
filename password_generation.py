

import random
import string
print("!PASSWORD GENERATOR!")


def ex():
    z = input("PRESS ANY BUTON FOR EXIT")#EXIT FUNCTION
    exit()


user_input = ""

while user_input != "-":

    user_input = input("Start program? Yes(1)/No(-)")

    if user_input == "1":
        print("SETTINGS:")

        try:
            adding_a_digit = int(input("Digits On? Yes(1)/No(2)"))
            adding_letters = int(input("Letters On? Yes(1)/No(2) "))
            adding_special_characters = int(
                input("Special characters On? Yes(1)/No(2)"))

            if adding_a_digit == adding_letters == adding_special_characters == 2:
                print("CHOOSE SOMETHING!!!")
                ex()

            if adding_a_digit == 1 or adding_a_digit == 2 and adding_letters == 1 or adding_letters == 2 or adding_special_characters == 1 or adding_special_characters == 2:
                user_password_length = int(
                    input("Write password length(max 30,min 6 ): "))
                if user_password_length > 30 or user_password_length < 6:
                    user_password_length = 30
                final_password = ""
                resultat_all = ""

                if adding_a_digit == 1:
                    resultat_all += "1234567890"

                if adding_letters == 1:
                    resultat_all += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

                if adding_special_characters == 1:
                    resultat_all += "!@#$%^&*()_'\\|?.,"

                N = 30  # КОЛИЧЕСТВО СИМВОЛОВ ПЕРЕД ИТОГОВЫМ ВЫБОРОМ!!!
                additional_choice = ""

                while N != 0:
                    additional_choice += random.choice(resultat_all)
                    N -= 1

                while user_password_length != 0:
                    final_password += random.choice(additional_choice)

                    user_password_length -= 1
                print(
                    f"YOUR PASSWORD: \n--------------------------------------------\n{final_password}\n--------------------------------------------")
            else:
                ex()
        except BaseException:
            print("ERROR!", EOFError)

    if user_input == "-":
        ex()
