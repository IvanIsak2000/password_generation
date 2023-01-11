# password generation
<div id="header" align="center">
  <img src="https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" width="100" height ="100"/>
 
</div>



EN
=======
MAIN
---
This program generates a password of a specified length according to the parameters you set.
You can set a password consisting of letters, numbers or special characters.

A welcome screen is displayed at startup, followed by a question: if you want to activate the program (press 1) or deactivate it (press minus).
>![image](https://user-images.githubusercontent.com/79650307/211566206-547f8a60-45ae-427d-9926-ab05bf7d4e7c.png)

GENERATION SETTINGS
---
If user entered one, generation settings will be shown:
1. First setting: should the password have digits, if yes then press 1, otherwise press 2.
2. Second setting: must the password have letters, if YES, then press 1, otherwise 2.
3. third setting: must the password include special characters, if yes, then 1, otherwise 2.



>![image](https://user-images.githubusercontent.com/79650307/211565999-accafe75-364e-4214-a910-34c8c127c18c.png)

If the conditions are correct, the programme asks for the length of the password. max length = 30 symbols, min length = 6, if the password is given as a number greater than 30 it becomes 30 symbols. If it is less than 6 it becomes 6.

ERROR HANDLING
-----
Outputs a message when an input error occurs:
>![image](https://user-images.githubusercontent.com/79650307/211568358-1993f941-d21b-4080-a6b0-ef8c7691c27e.png)
>
>In this case, the user has entered a character instead of a number which defines the length of the password and an error is therefore printed.

RESULT
---
If the entered values are correct, the program will generate a password and print it out:
>![image](https://user-images.githubusercontent.com/79650307/211569000-e4b0deb5-62a0-4cf6-93a4-a9cf3c1b9ea6.png)

COMPILATION
---
If you want to use the program with a .exe extension, copy the code, open any text editor, save it under password_generation.py. Then open a command prompt and type in the directory where you saved the program.
Then type **pip install pyinstaller** to install the library, once the installation is complete you can start compiling.To do this write **pyinstaller --onefile password_generation.py** 
The result is usually saved in **dict** folder: this will be our .exe file 🐍
>![image](https://user-images.githubusercontent.com/79650307/211572138-c7c60d1e-bab2-4c5e-9a89-ca350c232012.png)
>![image](https://user-images.githubusercontent.com/79650307/211572373-cf60a7e7-bcf5-4dc2-a4d5-27f0430c9187.png)

>More about the pyinstaller library: https://pypi.org/project/pyinstaller/



RU
=======
ОСНОВНОЕ
---
Эта программа генерирует пароль заданной длины в соответствии с заданными параметрами.
Вы можете установить пароль, состоящий из букв, цифр или специальных символов.

При запуске выводится приветствие, а после вопрос: включить программу (нажать цифру 1) или выключить (нажать минус)
>![image](https://user-images.githubusercontent.com/79650307/211566206-547f8a60-45ae-427d-9926-ab05bf7d4e7c.png)

НАСТРОЙКИ ГЕНЕРАЦИИ
---
Если пользователь ввёл единицу, то выводятся настройки генерации:
1. Первая настройка: должен ли пароль иметь цифры, если ДА, то нажать 1, иначе 2.
2. Вторая настройка: должен ли пароль иметь буквы, если ДА , то ввести 1, иначе 2.
3. Треть настройка: должен ли пароль включать специальные символы, если да , то 1, иначе 2.



>![image](https://user-images.githubusercontent.com/79650307/211565999-accafe75-364e-4214-a910-34c8c127c18c.png)

Если условия настройки заданы правильно , спрашивается, какой длины должен быть пароль.Максимальная длина = 30 символам, минимальная = 6, если пароль задан как число больше 30 , то пароль становиться 30 символов. Если  меньши 6, то 6.

ОБРАБОТКА ОШИБОК
-----
При возникновении ошибок ввода выводит сообщение :
>![image](https://user-images.githubusercontent.com/79650307/211568358-1993f941-d21b-4080-a6b0-ef8c7691c27e.png)
>
>В данном случае пользователь ввёл вместо числа, определяющего длину пароля, знак, следовательно напечаталась ошибка.

РЕЗУЛЬТАТ
---
Если всё было заданно правильно, то программа сгенерирует пароль и выведет его:
>![image](https://user-images.githubusercontent.com/79650307/211569000-e4b0deb5-62a0-4cf6-93a4-a9cf3c1b9ea6.png)

КОМПИЛЯЦИЯ
---
Если вы хотите использовать программу  в расширении .exe, то скопируйте код, откройте любой текстовый редактор, сохраните под названием password_generation.py. После откройте командную строку и пропишите директорию, в которой сохранилась программа.
Затем пропишите **pip3 install pyinstaller** для установки библиотеки, после завершени установки можно приступить к компиляции.Для этого напишите **pyinstaller --onefile password_generation.py** 
Результат обычно сохраняется в папке **dict**: там будет наш .exe файл 🐍
>![image](https://user-images.githubusercontent.com/79650307/211572138-c7c60d1e-bab2-4c5e-9a89-ca350c232012.png)
>![image](https://user-images.githubusercontent.com/79650307/211572373-cf60a7e7-bcf5-4dc2-a4d5-27f0430c9187.png)

>Больше о библиотеке pyinstaller: https://pypi.org/project/pyinstaller/
