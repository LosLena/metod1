import datetime

def log(s, elapsed=None):
    line = "="*40
    print(line)
    print(datetime.datetime.now(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print()

def endlog():
    end = datetime.datetime.now()
    elapsed = end-start
    log("Конец программы")
    line = "="*40
    print(line)
    print(f"{elapsed}, -Время выполнения программы")
    line = "="*40
    print(line)

start = datetime.datetime.now()
log("Старт программы")
age = int(input("Введите Ваш возраст: "))
sex = input("Введите Ваш пол м/ж: ")

if 18 <= age <=27 and sex.lower() == 'м':
  children_count = int(input("Введите количество детей: "))
  if children_count < 2:
    student_user = input("Учитесь ли вы сейчас да/нет: ")
    if student_user.lower() == "нет": 
        height_user = int(input("Введите Ваш рост в сантиметрах: "))
        if height_user >= 160:
          print("Вы годны в танковые войска")
        elif 150 <= height_user <160:
          print("Вы годны в десантные войска")
        elif 140 <= height_user <150:
          print("Вы годны в штаб")
        elif height_user < 140:
          print("Вы не подходите по росту для службы в армии")  
    else:
       print("Согласно о статьей 24 ФЗ № 53 «О воинской обязанности и военной службе» Вам полагается отсрочка")               
  else:
    print("Согласно о статьей 24 ФЗ № 53 «О воинской обязанности и военной службе» Вам полагается отсрочка")  
else:
  print("Согласно ФЗ № 53 «О воинской обязанности и военной службе» Вы не подходите для воинской службы")  



endlog()