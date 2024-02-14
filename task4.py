import csv

with open('vacancy.csv', encoding='utf8') as file:
    '''

    reader - открытие vacancy.csv
    data - считывание данных с файла
    company_ls - словарь состоящий из названия компании и максимальной заработной платой в ней
    company_work - словарь состоящий из названия компании и должностью с максимальной зп
    ls - список данных для подстановки в vacancy_new.csv
    lm - отсортированный список по зп

    '''
    reader = csv.reader(file)
    data = [x[0].split(';') for x in list(reader)][1:]
    type_of_work_sl = {}
    type_of_work_count = {}
    type_of_work_sr = {}
    for salary, wtype, size, role, comp_name in data:
        type_of_work_sl[wtype.upper()] = 0
        type_of_work_count[wtype.upper()] = 0
    for salary, wtype, size, role, comp_name in data:
        type_of_work_sl[wtype.upper()] = (int(type_of_work_sl[wtype.upper()]) + int(salary))
        type_of_work_count[wtype.upper()] += 1
    for salary, wtype, size, role, comp_name in data:
        type_of_work_sr[wtype.upper()] = type_of_work_sl[wtype.upper()]/type_of_work_count[wtype.upper()]
    ls = []
    for salary, wtype, size, role, comp_name in data:
        ls.append(str((int(salary)/(type_of_work_sr[wtype.upper()])) * 100)+'%')
    print(ls)
