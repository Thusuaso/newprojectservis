import time

def sure_hesapla_Args(func):
    def customMetot(args):
        baslangic = time.time()
        metod = func(args)
        bitis = time.time()
        print(f"{func.__name__} fonksiyon { bitis - baslangic } saniye sürdü.")
        return metod
    return customMetot


def sure_hesapla_Kwargs(func):
    def customMetot(args,kwargs):
        baslangic = time.time()
        metod = func(args,kwargs)
        bitis = time.time()
        print(f"{func.__name__} fonksiyon { bitis - baslangic } saniye sürdü.")
        return metod
    return customMetot