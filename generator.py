import string
import random
from datetime import date
import datetime



str1 = 'йцукенгшщзхъфывапролджэячсмитьбю'
str2 = str1.upper()
str3 = list(str1 + str2)
l_date = datetime.date(2016, 3, 4)
f_date = datetime.date.today()
delta = f_date.toordinal()
delta1 = l_date.toordinal()
for q in range(100):
    f = open('test%s.txt' %(q), 'w', encoding='utf-8')
    for i in range(100000):
        result = random.randint(1, delta - delta1) + delta1
        result1 = date.fromordinal(result)
        result1 = result1.strftime('%d.%m.%Y')
        latin = ''.join([random.choice(string.ascii_letters) for x in range(10)])
        rus = ''.join([random.choice(str3) for j in range(10)])
        numb = str(random.randint(1, 100000000))
        last = str(round((random.random() * 19), 8))
        f.write(result1 + '||' + latin + '||' + rus + '||' + numb + '||' + last + '||' + '\n')
    f.close()