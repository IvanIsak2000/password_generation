import random
import string
print("!PASSWORD GENERATOR!")


def ex():
    z = input("PRESS ANY BUTON FOR EXIT")
    exit()


an = ""

while an != "-":

    an = input("Start program? Yes(1)/No(-)")

    if an == "1":
        print("SETTINGS:")

        try:
            num = int(input("Number On? Yes(1)/No(2)"))
            letter = int(input("Letter On? Yes(1)/No(2) "))
            spec_char = int(input("Special characters? Yes(1)/No(2)"))

            if num == letter == spec_char == 2:
                print("CHOOSE SOMETHING!!!")
                ex()

            if num == 1 or num == 2 and letter == 1 or letter == 2 or spec_char == 1 or spec_char == 2:
                len_ = int(input("Write password length(max 30,min 6 ): "))
                if len_ > 30 or len_ < 6:
                    len_ = 30
                password = ""
                resultat_all = ""

                if num == 1:
                    resultat_all += "1234567890"

                if letter == 1:
                    resultat_all += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

                if spec_char == 1:
                    resultat_all += "!@#$%^&*()_'\\|?.,"

                N = 30
                pred_res = ""

                while N != 0:
                    pred_res += random.choice(resultat_all)
                    N -= 1

                while len_ != 0:
                    password += random.choice(pred_res)

                    len_ -= 1
                print(
                    f"YOUR PASSWORD: \n--------------------------------------------\n{password}\n--------------------------------------------")
            else:
                ex()
        except BaseException:
            print("ERROR!", EOFError)

    if an == "-":
        ex()
