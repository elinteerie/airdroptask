# myapp/management/commands/load_data.py
import os
import json
from django.core.management.base import BaseCommand
from airdrop.models import User  # Import your model here

class Command(BaseCommand):
    help = 'Load data from JSON file into Airdrop user models'

    def handle(self, *args, **kwargs):
        json_file_path = os.path.join('airdrop', 'fixtures', 'data.json')

        # Open and read the JSON file with UTF-8 encoding
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Loop through the data and create/update model instances
        for item in data:
            fields = item['fields']
            user, created = User.objects.get_or_create(
                pk=item['pk'],
                solana_wallet=fields['solana_wallet'],
                telegram_username=fields['telegram_username'],
                quote_retweet_link=fields['quote_retweet_link'],
                created_at=fields['created_at'],
                referral_count=fields['referral_count'],
                referral_id=fields['referral_id'],
                balance=fields['balance']
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))