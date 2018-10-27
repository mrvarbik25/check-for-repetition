with_out_turns = [] # обявление списков и констант
turns = []
template = 'Кол-во повторений: {0}\nПовторения: {1}'
text = []
choice = None

def split(string):
    """разбивка строки или файла"""
    for i in string: # перебор словаря 'x' со всеми словами
        if i not in with_out_turns: # если i нет в списке with_out_turns => записываем её туда
            with_out_turns.append(i)
        elif i in with_out_turns:   # если i есть в списке with_out_turns => записываем её в список "повторений"
            turns.append(i)

def write_in_file(choice, content): # запись в файл
    """функция записи в файл того что было передано в аргумент content"""
    if choice == 'yes':
        file = open('file_with_repetitions.txt', 'w')   #  создание файла
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
    split(string)   # разбивка текста из переменной string в словарь по символу разделителю
    if turns == []:                 # если список turns пустой то выводим "повторений нет"
        print('\nПовторений нет!')
    else:                           # иначе выводим: Повторения кол-во повторений, Без повторений
        print('\nПовторения: ' + str(len(turns)) + ' ' + str(turns))
        print('Без повторений: ' + str(with_out_turns))
        percent_calculator(turns, string)

def split_file():
    """разбивает файл по символу разделителю"""
    file_name = str(input('Название файла: '))
    file = open(file_name, 'r') # чтение файла в режиме read only
    text = file.read()  # чтение содержимого файла в переменную text
    file.close()
    text = text.split(choice_simvol_separator) # разбивка текста из переменной text в словарь по символу разделителю
    split(text) # вызов функции для разбивки переменной 'text' по символу разделителю в словарь
    write_in_file_choice = str(input('Записать повторения в файл?[yes/no]: '))  # спрашивает пользователя хочет ли он записать повторения в файл
    write_in_file(write_in_file_choice, template.format(len(turns), str(turns))) # запись в файл по шаблону и подстановка данных через метод format если пользователь ответил YES
    print_content(write_in_file_choice, template.format(len(turns), str(turns))) # вывод на экран по шаблону и подстановка данных через метод format если пользователь ответил NO

def ifchoice(choice):
    """проверка choice == 1 или 2
    и вызов соответствующей строки"""
    while choice == None:   # пока choice = None, если пользователь ввел НЕ 1 ИЛИ 2 а другое число тогда выход из программы
        choice = int(input('\nВыберите:\n1 - чтение строки\n2 - чтение файла\n>>> '))
        if choice == 1:     # чтение строки
            split_string()
        elif choice == 2:   # чтение файла
            split_file()

def welcome():
    """приветствие"""
    print('\nДобро пожаловать в программу "Повторения" \tauthor Yehor Varbanskiy.\nВведите символ разделитель.\nПример:\' \' или \',\'\n')

welcome()
choice_simvol_separator = str(input('Выберите сивол разделитель: '))    # ввод символ разделитель
ifchoice(choice)
