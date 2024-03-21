from django.shortcuts import render, redirect
from .forms import AirdropForm, UserForm
from django.urls import reverse
from .models import User
import os
from django.conf import settings
from django.http import HttpResponse

def airdrop_signup(request):
    if request.method == 'POST':
        form = AirdropForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.generate_referral_id()  # Generate referral ID for the user
            user.save()

            # Check if there is a referral ID in the form submission
            referral_id = referral_id = request.GET.get('referral_id')
            print(referral_id)
            if referral_id:
                try:
                    referred_user = User.objects.get(referral_id=referral_id)
                    referred_user.referral_count += 1
                    referred_user.balance += 10000
                    referred_user.save()
                except User.DoesNotExist:
                    pass  # Handle the case where the referral ID does not exist

            # Redirect or render success message
            return redirect(reverse('success') + '?referral_id=' + user.referral_id) # Redirect to a success page
    else:
        form = AirdropForm()
    return render(request, 'airdrop/signup.html', {'form': form})


def success_view(request):
    referral_id = request.GET.get('referral_id')
    referral_link = None
    if referral_id:
        referral_link = f"/airdrop/signup/?referral_id={referral_id}"
        balance = "650,000 $DREW"
        referal_count = "0"
    return render(request, 'airdrop/success.html', {'referral_id': referral_id, 'referral_link': referral_link, 'balance': balance, 'referal_count': referal_count})

def user_info(request):
    if request.method == 'POST':
        
        # Process form submission
        solana_wallet = request.POST.get('solana_wallet')
        try:
            user = User.objects.get(solana_wallet=solana_wallet)
            balance = user.balance
            referral_count = user.referral_count
            return render(request, 'airdrop/user.html', {'user': user, 'balance': balance, 'referral_count': referral_count})
        except User.DoesNotExist:
            return render(request, 'airdrop/user.html', {'error_message': 'User not found', 'solana_wallet': solana_wallet})
    else:
        # Render the form
        form = UserForm(request.POST)
        return render(request, 'airdrop/user.html', {'form': form})
    

def index_view(request):
    
    return render(request, 'airdrop/index.html')



def ads_txt_view(request):
    with open(os.path.join(settings.STATIC_ROOT, 'ads.txt')) as file:
        file_content = file.readlines()
    return HttpResponse(file_content, content_type="text/plain")