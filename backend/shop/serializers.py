from dataclasses import fields
from rest_framework import serializers 
from shop.models import *

class AuthorSer(serializers.ModelSerializer):
    class Meta: 
        model = Author
        fields = "__all__"

class PublisherSer(serializers.ModelSerializer):
    class Meta: 
        model = Publisher
        fields = "__all__"

class CategoryBookSer(serializers.ModelSerializer):
    class Meta: 
        model = CategoryBook
        fields = "__all__"

class BookSer(serializers.ModelSerializer):
    publisherId = PublisherSer(read_only=True)
    author = AuthorSer(many=True,read_only=True)
    categoryBookId = CategoryBookSer(read_only=True)
    class Meta: 
        model = Book
        fields = "__all__"

class BookItemSer(serializers.ModelSerializer):
    book = BookSer(read_only=True)
    class Meta: 
        model = BookItem
        fields = "__all__"

class MobilePhoneSer(serializers.ModelSerializer):
    class Meta: 
        model = MobilePhone
        fields = "__all__"

class MobilePhoneItemSer(serializers.ModelSerializer):
    mobilePhone = MobilePhoneSer(read_only=True)
    class Meta: 
        model = MobilePhoneItem
        fields = "__all__"

class CategoryClothesSer(serializers.ModelSerializer):
    class Meta: 
        model = CategoryClothes
        fields = "__all__"

class ShirtSer(serializers.ModelSerializer):
    class Meta: 
        model = Shirt
        fields = "__all__"

class DressSer(serializers.ModelSerializer):
    class Meta: 
        model = Dress
        fields = "__all__"

class PantSer(serializers.ModelSerializer):
    class Meta: 
        model = Pant
        fields = "__all__"

class ShirtSer(serializers.ModelSerializer):
    class Meta: 
        model = Shirt
        fields = "__all__"

class ClothesSer(serializers.ModelSerializer):
    category = CategoryClothesSer(read_only=True)
    class Meta: 
        model = Clothes
        fields = "__all__"

class ClothesItemSer(serializers.ModelSerializer):
    clothes = ClothesSer(read_only=True)
    class Meta: 
        model = ClothesItem
        fields = "__all__"

class PaymentSer(serializers.ModelSerializer):
    class Meta: 
        model = Payment
        fields = "__all__"

class ShipmentSer(serializers.ModelSerializer):
    class Meta: 
        model = Shipment
        fields = "__all__"

class AccountSer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields = "__all__"

class AddressSer(serializers.ModelSerializer):
    class Meta: 
        model = Address
        fields = "__all__"

class FullnameSer(serializers.ModelSerializer):
    class Meta: 
        model = FullName
        fields = "__all__"

class CustomerSer(serializers.ModelSerializer):
    account = AccountSer(read_only=True)
    fullname = FullnameSer(read_only=True)
    address = AddressSer(read_only=True)
    class Meta: 
        model = Customer
        fields = "__all__"

class VoucherSer(serializers.ModelSerializer):
    class Meta: 
        model = Voucher
        fields = "__all__"

class CPUSer(serializers.ModelSerializer):
    class Meta: 
        model = CPU
        fields = "__all__"

class VGASer(serializers.ModelSerializer):
    class Meta: 
        model = VGA
        fields = "__all__"

class LaptopSer(serializers.ModelSerializer):
    vga = VGASer(read_only=True)
    cpu = CPUSer(read_only=True)
    class Meta: 
        model = Laptop
        fields = "__all__"

class LaptopItemSer(serializers.ModelSerializer):
    laptop = LaptopSer(read_only=True)
    class Meta: 
        model = LaptopItem
        fields = "__all__"

class CartSer(serializers.ModelSerializer):
    laptops = LaptopItemSer(many=True,read_only=True)
    mobilePhones = MobilePhoneItemSer(many=True,read_only=True)
    clothes = ClothesItemSer(many=True,read_only=True)
    books = BookItemSer(many=True,read_only=True)
    class Meta: 
        model = Cart
        fields = "__all__"

class OrderSer(serializers.ModelSerializer):
    address = AddressSer(read_only=True)
    shipment = ShipmentSer(read_only=True)
    payment = PaymentSer(read_only=True)
    voucher = VoucherSer(many=True,read_only=True)
    customer = CustomerSer(read_only=True)
    cart = CartSer(read_only=True)
    class Meta: 
        model = Order
        fields = "__all__"
