def numeral():
    num = input("Enter a number:")

    #  списки для каждой строки
    nums_string1 = []
    nums_string2 = []
    nums_string3 = []
    nums_string4 = []
    nums_string5 = []

    #  строки с символами для каждой цифры
    string1 = ['***', '  *', '***', '***', '* *', '***', '***', '***', '***', '***']
    string2 = ['* *', '* *', '  *', '  *', '* *', '*  ', '*  ', '  *', '* *', '* *']
    string3 = ['* *', '  *', '***', '***', '***', '***', '***', ' * ', '***', '***']
    string4 = ['* *', '  *', '*  ', '  *', '  *', '  *', '* *', '*  ', '* *', '  *']
    string5 = [' * ', '  *', '***', '***', '  *', '***', '***', '*  ', '***', '***']

    for digit in num:  # цикл для каждой цифры и добавление в списки по индексу == цифре
        digit = int(digit)
        nums_string1.append(string1[digit])
        nums_string2.append(string2[digit])
        nums_string3.append(string3[digit])
        nums_string4.append(string4[digit])
        nums_string5.append(string5[digit])

    print('   '.join(nums_string1))
    print('   '.join(nums_string2))
    print('   '.join(nums_string3))
    print('   '.join(nums_string4))
    print('   '.join(nums_string5))

numeral()
