from .models import *
from django import forms


class PaymentRegistration(forms.ModelForm):
    class Meta:
        model = PaymentBreakUP
        fields = ['ID','Payment_Method','payment']
        # widgets = {
        # 	'ID': forms.NumberInput(attrs={'class': 'form-control','id':'bookingid'}),
            
        #     'Payment_Method': forms.TextInput(attrs={'class': 'form-control',
        #                                              'id': 'paymethodid'}),
        #     'payment': forms.NumberInput(attrs={'class': 'form-control',
        #                                         'id': 'paymentid'}),
        # }


# 'ID': forms.NumberInput(attrs={'class': 'form-control',
#                                            'id': 'bookingid'}),