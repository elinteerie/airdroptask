from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    solana_wallet = models.CharField(max_length=100, unique=True)
    telegram_username = models.CharField(max_length=100)
    quote_retweet_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    referral_count = models.IntegerField(default=0)
    referral_id = models.CharField(max_length=10, null=True, blank=True)
    balance = models.IntegerField(default=650000)

    def __str__(self):
        return self.solana_wallet
    
    def generate_referral_id(self):
        if not self.referral_id:
            self.referral_id = str(uuid.uuid4())[:10]  # Generate a unique referral ID
            self.save()