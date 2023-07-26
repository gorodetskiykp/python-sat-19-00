https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html

Рекомендации по написанию кода

- длина строки кода - не более 79 символов
- внутри скобок не ставятся пробелы после открывающей скобки и перед закрывающей
- после запятой поставь пробел, перед запятой - не надо
- вокруг знаков (операторов) ставим по одному пробелу (исключение - выделение приоритета)
- имена переменных 
    - английский язык 
    - маленькими буквами 
    - !!!нести смысловую нагрузку
    - переменные из нескольких слов используют символ подчеркивания (snake_case)


E501 line too long (96 > 79 characters)

E261 at least two spaces before inline comment\
Между кодом и комментарием должно быть 2 пробела

E262 inline comment should start with '# '\
После знака # нужен пробел

W292 no newline at end of file\
В конце файла одна пустая строка
 
E225 missing whitespace around operator\
Операторы обособляются пробелами

E231 missing whitespace after ','\
После запятой нужен пробел (до запятой - не нужен)

E128 continuation line under-indented for visual indent\
При переносе строки операции не соблюдены отступы
