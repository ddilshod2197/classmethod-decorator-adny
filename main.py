class Arxitektor:
    def __init__(self, ism, familiya, tajriba):
        self.ism = ism
        self.familiya = familiya
        self.tajriba = tajriba

    @classmethod
    def yangi_arxitektor(cls, ism, familiya, tajriba):
        return cls(ism, familiya, tajriba)

arxitektor1 = Arxitektor("Ali", "Valiyev", 10)
arxitektor2 = Arxitektor.yangi_arxitektor("Vali", "Aliyev", 5)

print(arxitektor1.ism)  # Ali
print(arxitektor1.familiya)  # Valiyev
print(arxitektor1.tajriba)  # 10

print(arxitektor2.ism)  # Vali
print(arxitektor2.familiya)  # Aliyev
print(arxitektor2.tajriba)  # 5
```

@classmethod metodni quyidagilar uchun ishlatish mumkin:

- Klass metodlarini yaratish uchun
- Klass metodlarini chaqirish uchun
- Klass metodlarining o'zaro aloqalarini yaratish uchun
- Klass metodlarining o'zaro aloqalarini chaqirish uchun
