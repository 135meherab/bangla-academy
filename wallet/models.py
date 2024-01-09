from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)

class WalletRecharge(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)