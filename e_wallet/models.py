from django.db import models

# Create your models here.


class User(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=55, blank=False, null=False)
    email = models.EmailField(default='', blank=False, null=False)
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('TRANSFER', 'TRANSFER'),
        ('AIRTIME', 'AIRTIME'),
        ('DATA', 'DATA'),
        ('BILLS', 'BILLS')
    ]

    TRANSACTION_STATUS = [
        ('SUCCESSFUL', 'SUCCESSFUL'),
        ('FAILED', 'FAILED'),
        ('PENDING', 'PENDING')
    ]
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default='')
    transaction_status = models.CharField(max_length=15, choices=TRANSACTION_STATUS, default='')
    amount = models.DecimalField(max_digits=9, decimal_places=2, default='')
    trans_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='wallet')
    beneficiary = models.ForeignKey('Beneficiary', on_delete=models.CASCADE, related_name='beneficiary')


class Account(models.Model):
    BANK_NAME = [
        ('UBA', 'UBA'),
        ('FIDELITY', 'FIDELITY'),
        ('FCMB', 'FCMB'),
        ('FBN', 'FBN'),
        ('ZENITH', 'ZENITH'),
        ('GTB', 'GTB')
    ]
    account_name = models.CharField(max_length=255, blank=False, null=False)
    account_number = models.CharField(max_length=10, blank=False, null=False)
    bank_name = models.CharField(max_length=255, choices=BANK_NAME, default='')


class CreditCard(models.Model):
    card_number = models.CharField(max_length=16, blank=False, null=False)
    expiry_date = models.DateField(blank=False, null=False)
    cvv = models.CharField(max_length=3, blank=False, null=False)


class Wallet(models.Model):
    balance = models.DecimalField(max_digits=6, decimal_places=2, default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')


class Beneficiary(models.Model):
    account_number = models.CharField(max_length=10, blank=False, null=False)
