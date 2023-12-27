# import random
# def f():
#  x=random.randint(1,50)
#  y=random.randint(1,50)
#  z=int(input(str(x)+" + "+str(y)+" = "))
#  if z==x+y :
#   print("To'g'ri")
#   f()
#  else:
#   print("Notug'ri")
#   f()
# f()




import re

def hisobla(ifoda):
    try:
        return eval(ifoda)
    except Exception as e:
        return f"Hisoblashda xatolik: {str(e)}"

while True:
    foydalanuvchi_kiritsin = input("son kiriting: ")

    if foydalanuvchi_kiritsin.lower() == 'exit':
        print("Dasturdan chiqilyapti.")
        break

    # Foydalanuvchi kiritgan ifoda faqat sonlar va asosiy matematik operatorlarni qabul qilish uchun tekshirish
    if not re.match("[0-9+\-*/(). ]+$", foydalanuvchi_kiritsin):
        print("Noto'g'ri belgi. Iltimos, faqat raqamlar va asosiy matematik belgilarni kiriting.")
        continue

    natija = hisobla(foydalanuvchi_kiritsin)
    print(f"Natija: {natija}")