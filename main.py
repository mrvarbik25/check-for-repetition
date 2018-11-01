# program to check for repetition.
# example to run with arguments: python3 main.py namefile.txt space no
import sys
import os
template = 'Кол-во повторений: {0}\nПовторения: {1}'
with_out_turns = [] # обявление списков и констант
turns = []
text = []
choice_simvol_separator = None
file_name = None

def work_with_args():
    args = sys.argv[1:]
    if args[1] == 'space':  # если во втором аргументе указано 'space' то заменить это на символ пробела ' '
        args.pop(1)
        args.insert(1, ' ')
    if args:    # если в аргументы что то передано
        if os.path.exists(args[0]): # если указан верный путь к файлу
            try:
                file_name = args[0] # присвоить к переменной file_name значение первого аргумента
                with open(file_name) as file:  # открыть файл для чтения
                    text = file.read()
                    text = text.split(args[1])
                    sort_function(text) # сортировка на повторения
                    if args[2] == 'no': # если третий аргумент = no, просто вывести на экран
                        print_content('no', template.format(len(turns), str(turns)))
                    if args[2] == 'yes':    # если третий аргумент = yes, то записать в файл с повторениями
                        if '/' in args[0]:    # если указан путь к файлу
                            index = args[0].rfind('/')    # записываем индекс самого правого символа '/'
                            file_with_repetitions = args[0][:index + 1] + 'file_with_repetitions.txt' # и посредством среза узнаем путь к файлу а посредством конкатенации добавляем имя file_with_repetitions.txt и записываем файл с повторениями туда (/some/path/file_with_repetitions.txt)
                            with open(file_with_repetitions, 'w') as file:  #  создание файла
                                file.write(template.format(len(turns), str(turns))) # записать в файл шаблон
                                print('Повторения записаны в файл \'file_with_repetitions.txt\'')
                        else:   # если указано имя файла а не путь к нему
                            with open('file_with_repetitions.txt', 'w') as file:  #  создание файла
                                file.write(template.format(len(turns), str(turns))) # запись в файл temlpate
                            print('Повторения записаны в файл \'file_with_repetitions.txt\'')
            except IndexError:  # если переданы не все аргументы
                print('[ Error ] [ NotAllArgumentsSpecified ]')
                print('Try this: python3 main.py path_to_file space [write repetitions to file? or just display? yes / no]')
        else:   # если указан неверный путь к файлу
            print('[ file not found ]')

def sort_function(string):
    """сортировка строки или файла в списки"""
    for i in string: # перебор словаря 'x' со всеми словами
        if i not in with_out_turns: # если i нет в списке with_out_turns => записываем её туда
            with_out_turns.append(i)
        elif i in with_out_turns:   # если i есть в списке with_out_turns => записываем её в список "повторений"
            turns.append(i)

def write_in_file(choice, content): # запись в файл
    """функция записи в файл того, что было передано в аргумент content"""
    if choice == 'yes':
        if '/' in file_name:    # если указан путь к файлу
            index = file_name.rfind('/')    # записываем индекс самого правого символа '/'
            file_with_repetitions = file_name[:index + 1] + 'file_with_repetitions.txt' # и посредством среза узнаем путь к файлу а посредством конкатенации добавляем имя file_with_repetitions.txt и записываем файл с повторениями туда (/some/path/filename.txt)
        file = open(file_with_repetitions, 'w')   #  создание файла
        file.write(content) # запись в файл то что передано в аргумент content
        print('Повторения записаны в файл \'file_with_repetitions.txt\'')
    elif choice == 'no':
        pass

def print_content(choice, content): # вывод на экран
    """выводит content на экран"""
    if choice == 'no':
        print(content)

def percent_calculator(desired_part, integer):
    """калькулятор процентов"""
    template = 'Повторения в процентах: {0}%'
    print(template.format(int(min(len(desired_part), len(integer)) / max(len(desired_part), len(integer)) * 100)))

def split_string():
    """разбивает строку по символу разделителю"""
    string = input() # ввод строки
    string = string.split(choice_simvol_separator) # разбивка в словарь по символу разделителю
    sort_function(string)   # разбивка текста из переменной string в словарь по символу разделителю
    if turns == []:                 # если список turns пустой то выводим "повторений нет"
        print('\nПовторений нет!')
    else:                           # иначе выводим: Повторения кол-во повторений, Без повторений
        print('\nПовторения: ' + str(len(turns)) + ' ' + str(turns))
        print('Без повторений: ' + str(with_out_turns))
        percent_calculator(turns, string)

def split_file():
    """разбивает файл по символу разделителю"""
    global file_name
    file_name = str(input('Название или путь к файлу: '))
    file = open(file_name, 'r') # чтение файла в режиме read only
    text = file.read()  # чтение содержимого файла в переменную text
    file.close()
    text = text.split(choice_simvol_separator) # разбивка текста из переменной text в словарь по символу разделителю
    sort_function(text) # вызов функции для разбивки переменной 'text' по символу разделителю в словарь
    write_in_file_choice = str(input('Записать повторения в файл?[yes/no]: '))  # спрашивает пользователя хочет ли он записать повторения в файл
    write_in_file(write_in_file_choice, template.format(len(turns), str(turns))) # запись в файл по шаблону и подстановка данных через метод format если пользователь ответил YES
    print_content(write_in_file_choice, template.format(len(turns), str(turns))) # вывод на экран по шаблону и подстановка данных через метод format если пользователь ответил NO

def ifchoice():
    """выбор символа разделителя,
    проверка choice == 1 или 2"""
    try:
        choice_simvol_separator = str(input('Выберите сивол разделитель: '))    # ввод символ разделитель
        if not choice_simvol_separator: # если пользователь не ввел ничего тогда выйти из программы, так как пустые строки в python = False
            print('[ Error ]\nError type: NoSeparatorCharacterSelected')
            raise SystemExit    # вызов исключения ( если choice_simvol_separator  - пустой ) для выхода
        choice = input('\nВыберите:\n1 - чтение строки\n2 - чтение файла\n>>> ')
        if not choice:  # вызов исключения ( если choice - пустой ) для выхода
            print('[ Error ]\nError type: NotOneItemSelected')
            raise SystemExit
        if choice == '1':     # чтение строки
            split_string()
        elif choice == '2':   # чтение файла
            split_file()
    except KeyboardInterrupt:   # при завершении программы выводить вместо ошибки - [ stopped ]
        print('\n[ stopped ]')
        raise SystemExit    # вызов исключения для выхода

def welcome():
    """приветствие"""
    print('\nДобро пожаловать в программу "Повторения" \tauthor Yehor Varbanskiy.\nВведите символ разделитель.\nПример:\' \' или \',\'\n')

def main():
    welcome()
    ifchoice()

if __name__ == '__main__':
    work_with_args()
    if sys.argv[1:] == []:  # если аргументов нет тогда обычный запуск
        main()
