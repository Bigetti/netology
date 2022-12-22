directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

x1 = "p"
x2 = 's'
x3 = 'l'
x4 = 'a'
x5 = 'd'
x6 = 'm'
x7 = 'n'
sh = False


### функция по p
def people(documents):
    txt = input('Введите номер документа, чтобы узнать ФИО Владельца: ')
    var = False
    for document in documents:
        if document['number'] == txt:
            var = True
            return document['name']
            break
    if var == False:
        # print("There are no such numbers")
        return "Нет таких граждан в базе"


### функция по s
def find_me(shef_reqest):
    var = False
    for key, value in directories.items():
        if shef_reqest in value:
            var = True
            return "На полке", key
    if var == False:
        # print("There are no such numbers")
        return "В нашей базе нет таких документов"
        # else:
        # return "There are no such shelves"
    # Проход по .items() возвращает кортеж (ключ, значение),
    # который присваивается кортежу переменных key, value
    # print(key, value, shef_reqest)


### функция по l  выводит весь список документов
def make_list(documents):
    for document in documents:
        valuesList = list(document.values())
        print(', '.join(valuesList))


#  for document in documents:
#    for value in document.values():
#      print(value)

### функция по a, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add_doc(documents, directories):
    dict_new_doc = {}
    dict_new_doc["type"] = input('Введите тип документа : ')
    dict_new_doc["number"] = input('Введите номер документа : ')
    dict_new_doc["name"] = input('Введите Имя и Фамилию: ')

    var = 0
    nomer_polki = input('Введите номер полки, на который положить документ, от 1 до 3: ')
    print('Вы выбрали полку номер', nomer_polki)
    print('Всего у нас в наличии полок: ', len(directories))
    for key, in directories:
        if nomer_polki == key and int(nomer_polki) > 0 and int(nomer_polki) <= len(directories):
            print("Est takaya polka and we added your document on it")
            documents.append(dict_new_doc)
            print('Актуальный список документов: ', documents)
            var = 1
            print(var)
            directories[key].append(dict_new_doc["number"])
            print('Актуальный список полок: ', directories)
            return var

    if var == 0:
        print('No such polka exist')

    # print (dict_new_doc)
    # print(documents)


### функция по d, delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
def del_doc(documents, directories):
    txt = input('Введите номер документа, чтобы удалить его из базы: ')
    alter = False
    for document in documents:
        if document['number'] == txt:
            documents.remove(document)
            print('Look now,  we just removed it', documents)
            alter = True
            for k, value in directories.items():
                # print(k)
                # print(value)
                for i in value:
                    if txt == i:
                        print('We found it on shelve', k)
                        value.remove(i)

    print('Tghought can see that there is no such document on shelves', directories)
    if alter == False:
        print('We didnt find such doc and it is nothing to remove')


# команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую это - m
def move_doc(documents, directories):
    alt = False
    x = input('Введите плиз номер документа: ')
    y = input('Введите плиз номер целевой полки, на которую переместить документ: ')

    #print(x, y)
    try:
        var = int(y)
        print("Ищем ищем...: ", y)
    except ValueError:
        print('Нужно номер полки сказать, а не то что вы промычали!')
        return
    var = int(y)
    if (var > len(directories)):
        #print(len(directories))
        print("Нет таких полок у нас к сожалению. Попробуйте выбрать из имеющихся от 1 до 3")
        import sys
        sys.exit()
    else:
        print('Попробуем найти Ваш документ и переместить в нужный каталог')

    for document in documents:
        if document['number'] == x:
            alt = True
            print("Документ принадлежит", document['name'])
            for k, value in directories.items():
                #print(k)
                #print(value)
                for i in value:
                    if x == i:
                        #print(i)
                        value.remove(i)
                        if x not in directories:
                            directories[y].append(x)

    if alt == False:
        print('Таких документов нет в нашей базе')
    else:
        print("Вот так теперь выглядят полки с документами", directories)

        # команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;


def add_shelf(directories):
    num = input('Введите пожалуйста номер новой полки!:  ')
    try:
        val = int(num)
        print(" Сейчас посмотрим можем ли мы создать  для Ваших целей  полку номер: ", num)
    except ValueError:
        print('"Это не номер а кликуха Вашей бабушки, введите номер, это же просто!')
        return

    if (int(num) > 100):
        print('Слишком большой порядковый номер или Вы ввели некорректный символ')
        return 'Fuck'

    if (int(num)):

        for key in directories:
            #print(key, num)
            if key == num:
                print("Полка с таким именем уже существует, попробуйте создать полку с новым уникальным номером")
                # import sys
                # sys.exit()
                return

        for key in directories:
            if num != key:
                directories[num] = []
                print("Добавили полку с вашим именем")
                return directories

    # Entering the chouse of letter


letter = input('Сделайте, пожалуйста выбор необходимой услуги:\n Нажмите p, чтобы получить имя человека, которому принадлежит документ\n'
' ЛИБО Нажмите s, чтобы узнать номер полки, на которой документ находится,\n '
'ЛИБО Нажмите l, чтобы получить список всех документов в формате passport "2207 876234" "Василий Гупкин",'
'\n ЛИБО Нажмите a, чтобы добавить новый документ в каталог и в перечень полок,'
' Вам придется ввести номер документа, тип, имя владельца и номер полки, на которой он будет храниться,'
'\n если же вы ходите удалить документ из каталога и с полок, нажмите d,'
' \n команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую это - m.'
' \nКоманда, которая спросит номер новой полки и добавит ее в перечень -- n. :')


print(letter)

if letter == x1:
    print(people(documents))
elif letter == x2:
    shef_reqest = input('Введите номер документа, чтобы узнать на какой полке он находится: ')
    print('документ номер', shef_reqest, ' ищем, подождите : ', find_me(shef_reqest))
elif letter == x3:
    make_list(documents)
elif letter == x4:
    add_doc(documents, directories)
    # print("sh")
    if sh == True:
        print('there are maximum 3 shelfs, try again')
elif letter == x5:
    del_doc(documents, directories)

elif letter == x6:
    move_doc(documents, directories)
elif letter == x7:
    add_shelf(directories)
    print("Вот список полок: ", directories)
else:
    print('Вы ввели какую-то хрень')
