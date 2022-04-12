from distutils.command.upload import upload
from statistics import mode
from MySQLdb import Timestamp
from django.db import models


class Author(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255)  
    biography = models.CharField(max_length=255) 

    def __str__(self):
        return self.name
    class Meta:  
        db_table = "author"  

class CategoryBook(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255) 
    def __str__(self):
        return self.name  
    class Meta:  
        db_table = "categorybook"

class Publisher(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255)  
    address = models.CharField(max_length=255)  
    def __str__(self):
        return self.name   
    class Meta:  
        db_table = "publisher"

class Book(models.Model):  
    id = models.AutoField(primary_key='true') 
    title = models.CharField(max_length=255)  
    language = models.CharField(max_length=255)
    numberOfPage = models.IntegerField()
    publicationDate = models.DateField(auto_created=True)
    categoryBookId = models.ForeignKey(CategoryBook,on_delete=models.CASCADE)
    publisherId = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    def __str__(self):
        return self.title
    class Meta:  
        db_table = "book"

class BookItem(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()
    description = models.CharField(max_length=255)
    numberSold = models.IntegerField()
    numAvailidInStock = models.IntegerField()
    images = models.ImageField(upload_to='backend/shop/uploads')
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    class Meta:
        db_table = "bookitem"

# class Image(models.Model):
#     id = models.AutoField(primary_key='true')
#     path = models.ImageField(upload_to='backend/shop/uploads')
#     bookItem = models.ForeignKey(BookItem,on_delete=models.CASCADE)
#     class Meta:
#         db_table = "images"

class MobilePhone(models.Model):  
    id = models.AutoField(primary_key='true') 
    name = models.CharField(max_length=255)  
    brand = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)  
    cpu = models.CharField(max_length=255)
    screen = models.CharField(max_length=255)  
    rearCamera = models.CharField(max_length=255)
    frontCamera = models.CharField(max_length=255)  
    color = models.CharField(max_length=255)
    ops = models.CharField(max_length=255)  
    battery = models.CharField(max_length=255)
    warranty = models.CharField(max_length=255)  
    size = models.CharField(max_length=255)
    displayType = models.CharField(max_length=255)  
    def __str__(self):
        return self.name
    class Meta:  
        db_table = "mobilephone"

class MobilePhoneItem(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()
    description = models.CharField(max_length=255)
    numberSold = models.IntegerField()
    numAvailidInStock = models.IntegerField()
    images = models.ImageField(upload_to='backend/shop/uploads')
    mobilePhone = models.ForeignKey(MobilePhone,on_delete=models.CASCADE)
    class Meta:
        db_table = "mobilephoneitem"

class CategoryClothes(models.Model):  
    id = models.AutoField(primary_key='true') 
    type = models.CharField(max_length=255) 
    def __str__(self):
        return self.name  
    class Meta:  
        db_table = "categoryclothes"


class Clothes(models.Model):  
    id = models.AutoField(primary_key='true') 
    productName = models.CharField(max_length=255)  
    marterial = models.CharField(max_length=255)
    countryOfOrigin = models.CharField(max_length=255)  
    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=255)  
    importPrice = models.FloatField()
    color = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryClothes,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:  
        db_table = "clothes"

class Shirt(Clothes):
    shirtId = models.AutoField(primary_key='true')
    sleevesLength = models.FloatField()
    chestMeasurements = models.FloatField()
    length = models.FloatField()
    collarType = models.CharField(max_length=255)
    def __str__(self):
        return self.collarType
    class Meta:  
        db_table = "shirt"

class Dress(Clothes):
    dressId = models.AutoField(primary_key='true')
    typeSleeves = models.CharField(max_length=255)
    chestMeasurements = models.FloatField()
    waistMeasurements = models.FloatField()
    buttMeasurements = models.FloatField()
    length = models.FloatField()
    shape = models.CharField(max_length=255)
    class Meta:  
        db_table = "dress"

class Pant(Clothes):
    paintId = models.AutoField(primary_key='true')
    thighMeasurements = models.FloatField()
    waistMeasurements = models.FloatField()
    buttMeasurements = models.FloatField()
    length = models.FloatField()
    class Meta:  
        db_table = "pant"

class Skirt(Clothes):
    skirtId = models.AutoField(primary_key='true')
    type = models.CharField(max_length=255)
    waistMeasurements = models.FloatField()
    buttMeasurements = models.FloatField()
    length = models.FloatField()
    class Meta:  
        db_table = "skirt"


class ClothesItem(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()
    description = models.CharField(max_length=255)
    numberSold = models.IntegerField()
    numAvailidInStock = models.IntegerField()
    images = models.ImageField(upload_to='backend/shop/uploads')
    clothes = models.ForeignKey(Clothes,on_delete=models.CASCADE)
    class Meta:
        db_table = "clothesitem"



class Payment(models.Model):
    id = models.AutoField(primary_key='true')
    type = models.CharField(max_length=255)
    class Meta: 
        db_table = "payment"

class Shipment(models.Model):
    id = models.AutoField(primary_key='true')
    cost = models.FloatField()
    type = models.CharField(max_length=255)
    class Meta:
        db_table = "shipment"

class Account(models.Model):
    id = models.AutoField(primary_key='true')
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = "account"

class Address(models.Model):
    id = models.AutoField(primary_key='true')
    numberHouse = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    class Meta:
        db_table = "address"

class FullName(models.Model):
    id = models.AutoField(primary_key='true')
    fisrtName = models.CharField(max_length=255)
    midName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    class Meta:
        db_table = "fullname"

class Customer(models.Model):
    id = models.AutoField(primary_key='true')
    phone = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    fullName = models.ForeignKey(FullName,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    class Meta:
        db_table = "customer"

class Voucher(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)
    discountPercent = models.FloatField()
    description = models.CharField(max_length=255)
    class Meta:
        db_table = "voucher"



class CPU(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)  
    techType = models.CharField(max_length=255)
    typeCpu = models.CharField(max_length=255)  
    speed = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)  
    def __str__(self):
        return self.name
    class Meta:
        db_table = "cpu"

class VGA(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)  
    vram = models.CharField(max_length=255)
    tech = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)  
    def __str__(self):
        return self.name
    class Meta:
        db_table = "vga"

class Laptop(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)  
    screen = models.CharField(max_length=255)
    battery = models.CharField(max_length=255)  
    weight = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    material = models.CharField(max_length=255)  
    warranty = models.CharField(max_length=255)
    ops = models.CharField(max_length=255)
    size = models.CharField(max_length=255)   
    ram =  models.CharField(max_length=255) 
    vga = models.ForeignKey(VGA, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "laptop"

class LaptopItem(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()
    description = models.CharField(max_length=255)
    numberSold = models.IntegerField()
    numAvailidInStock = models.IntegerField()
    images = models.ImageField(upload_to='backend/shop/uploads')
    laptop = models.ForeignKey(Laptop,on_delete=models.CASCADE)
    class Meta:
        db_table = "laptopitem"

class Cart(models.Model):
    id = models.AutoField(primary_key = 'true')
    quantity = models.FloatField()
    totalPrice = models.FloatField()
    books = models.ManyToManyField(BookItem)
    clothes = models.ManyToManyField(ClothesItem)
    mobliePhones = models.ManyToManyField(MobilePhoneItem)
    laptops = models.ManyToManyField(LaptopItem)
    class Meta:
        db_table = "cart"


class Order(models.Model):
    id = models.AutoField(primary_key='true')
    status = models.CharField(max_length=255)
    totalAmount = models.FloatField()
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    voucher = models.ManyToManyField(Voucher)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    class Meta:
        db_table = "order"