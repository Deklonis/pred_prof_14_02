import csv
input_name = input('Введите название компании: ')
with open('vacancy.csv', encoding='utf8') as file:
    '''

    reader - открытие vacancy.csv
    data - считывание данных с файла
    company_ls - словарь состоящий из названия компании и максимальной заработной платой в ней
    company_work - словарь состоящий из названия компании и должностью с максимальной зп
    ls - список данных для подстановки в vacancy_new.csv
    

    '''
    reader = csv.reader(file)
    data = [x[0].split(';') for x in list(reader)][1:]
    company_sl = {}
    company_work = {}
    for salary, wtype, size, role, comp_name in data:
        company_sl[comp_name] = 0
    for salary, wtype, size, role, comp_name in data:
        company_sl[comp_name] = max(int(salary), int(company_sl[comp_name]))
    for salary, wtype, size, role, comp_name in data:
        if company_sl[comp_name] == int(salary):
            company_work[comp_name] = role
    ls = []
    for x in list(company_sl.items()):
        ls.append([x[0], company_work[x[0]], x[1]])
    while input_name != 'None':
        if input_name in [x[0] for x in list(company_work.items())]:
            print(f'В {input_name} найдена вакансия: {company_work[input_name]}. З/п составит: {company_sl[input_name]}')
        else:
            print('К сожалению, ничего не удалось найти')
        input_name = input('Введите название компании: ')