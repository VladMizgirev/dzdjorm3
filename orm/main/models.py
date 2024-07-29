from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id =  models.IntegerField(primary_key=True)
    model = models.CharField(max_length=50, null= True)
    year = models.IntegerField(null= True)
    color = models.CharField(max_length=50, null= True)
    mileage = models.IntegerField(null= True)
    volume = models.DecimalField(max_digits=2, decimal_places=1, null= True)
    body_type = models.CharField(choices=BODY_TYPE_CHOICES, blank=True) #тип кузова, варианты возможных значений взять из BODY_TYPE_CHOICES;
    drive_unit = models.CharField(choices=DRIVE_UNIT_CHOICES, blank=True) #привод, варианты возможных значений взять из DRIVE_UNIT_CHOICES;
    gearbox = models.CharField(choices=GEARBOX_CHOICES, blank=True) #коробка передач, варианты возможных значений взять из GEARBOX_CHOICES;
    fuel_type = models.CharField(choices=FUEL_TYPE_CHOICES, blank=True) #тип топлива, варианты возможных значений взять из FUEL_TYPE_CHOICES;
    price = models.IntegerField(null= True)
    image = models.ImageField(blank= True, null= True)

    def __str__(self):
        return f'{self.model} {self.year} {self.price}'


class Sale(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null= True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null= True)
    created_at = models.DateField(auto_now_add=True, null= True) #дата и время продажи, для автозаполнения добавьте свойство auto_now_add=True.

    def __str__(self):
        return f'{self.id} {self.client} {self.car} {self.created_at}'
