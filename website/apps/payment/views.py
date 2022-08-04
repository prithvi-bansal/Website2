from django.shortcuts import render
from django.conf import settings

import stripe
stripe.api_key = 'sk_test_51LSxHwSHRENcAYQVgIuvOn2KLvbkd4CC6Bbes1s8UsaAthJe1aTAucBoK6VJ5QzU5cCnLq3sdrBPKMjWGSGfhpl100frHodmpP'

# Create your views here.
def payment(request):
	key = settings.STRIPE_PUBLISHABLE_KEY
	return render(request, 'payment/payment.html', {'key':key})

def charge(request):

	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		stripe.PaymentIntent.create(
		 	amount=amount,
		  	currency="usd",
		  	payment_method_types=["card"],
		)

	return render(request, 'payment/success.html')