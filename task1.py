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

with open('vacancy_new.csv', 'w') as file:
    '''
    
    Записываем значения в vacancy_new.csv
    
    '''
    w = csv.writer(file)
    w.writerow(['company', 'role', 'Salary'])
    for i in ls:
        w.writerow(i)
lm = sorted(ls, key=lambda x: int(x[2]), reverse=True)
for i in range(3):
    print(lm[i][0], lm[i][1], lm[i][2])