app=str(input('اسم برنامه ای که میخوای استفاده کنی رو وارد کن :', ))
if app=='روز و ماه':
    m = int(input("ماه رو وارد کن:", ))
    d = int(input("روز رو وارد کن:", ))
    if m<=7:
        s = (m-1)*31+d
    else:
        s=(m-1)*30+6+d
    days=["شنبه","یکشنبه","دوشنبه","سه شنبه","چهار شنبه","پنجشنبه","جمعه"]
    print(days[s%7])
elif app=='اعداد شگفت انگیز':
    n=int(input("مقدار سطر هاتو وارد کن:", ))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
elif app=='ستاره های شگفت انگیز':
    n=int(input("مقدار سطر هاتو وارد کن:", ))
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print()
elif app=="زوج یا فرد!":
    n=int(input('عددی که میخوای امتحان کنی رو وارد کن:', ))
    if n % 2 == 0:
        print("عدد مورد نظر شما زوج است")
    else:
        print('عدد موزد نظر شما فرد است')
elif app=="نمره سنج":
    n=float(input("معدلی که میخوای بسنجی رو وارد کن:", ))
    if 17 <= n <= 20:
        print('خیلی خوب!')
    elif 14 <= n <= 16:
            print('خوب')
    elif 9 <= n <= 13:
            print('قابل قیول')
    elif 0 <= n <= 8:
            print('نیاز به تلاش بیشتر')
elif app=='فیبوناچی':
    def Fibonachi(n):
        if n < 0:
            print("Incorrect input")
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return Fibonachi(n - 1) + Fibonachi(n - 2)
    x=int(input("چندمین جمله دنباله فیبوناچی رو میخوای بدونی:", ))
    print(f'دنباله {x}ام فیبوناچی{Fibonachi(x)}هستش')
elif app=="خروج":
    print("مرسی که از برنامه استفاده کردی ^^")
    print()
    print("ورژن فعلی:1.0")
    print()
    print("روز یا شب خوبی داشته باشی!!!!")
else:
    print("ببخشید این برنامه هنوز موجود نیست ولی شاید تو بروزرسانی بعد اضافه کنیمش")
    print("*****************")
    print("اگر میتونید برنامه پیشنهادیتون رو به ما بگید ما سعیمون رو میکینم تو بروزرسانی بعدی اضافش کنیم")