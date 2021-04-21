from django import forms

from sales.models import Salesbooking


class bookingform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(bookingform, self).__init__(*args, **kwargs)
        self.fields['booking_ID'].widget.attrs['readonly'] = True
        self.fields['customer_name'].widget.attrs['readonly'] = True
        self.fields['contact_number'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['Brand'].widget.attrs['readonly'] = True
        self.fields['Model'].widget.attrs['readonly'] = True
        self.fields['Variant'].widget.attrs['readonly'] = True
        self.fields['Colour'].widget.attrs['readonly'] = True
        self.fields['Ex_Showroom_Price'].widget.attrs['readonly'] = True
        self.fields['Insurance_AMT'].widget.attrs['readonly'] = True
        self.fields['RTO'].widget.attrs['readonly'] = True
        self.fields['FASTAG'].widget.attrs['readonly'] = True
        self.fields['TCS'].widget.attrs['readonly'] = True
        self.fields['ACCESSORIES'].widget.attrs['readonly'] = True
        self.fields['Extended_Warranty'].widget.attrs['readonly'] = True
        self.fields['Annual_Maintanence_Cost'].widget.attrs['readonly'] = True
        self.fields['On_Road_Price'].widget.attrs['readonly'] = True
        self.fields['booking_receipt'].widget.attrs['readonly'] = True
        self.fields['quotation'].widget.attrs['readonly'] = True
        self.fields['order_form'].widget.attrs['readonly'] = True
        self.fields['Delivery_Order'].widget.attrs['readonly'] = True
        self.fields['Consumer_offer'].widget.attrs['readonly'] = True
        self.fields['Exchange_bonus'].widget.attrs['readonly'] = True
        self.fields['Corporate_discount'].widget.attrs['readonly'] = True
        self.fields['Remarks'].widget.attrs['readonly'] = True
        self.fields['Dealer_discount'].widget.attrs['readonly'] = True
        self.fields['Total_discount'].widget.attrs['readonly'] = True
        self.fields['Down_Payment'].widget.attrs['readonly'] = True
        self.fields['Finance'].widget.attrs['readonly'] = True
        self.fields['Used_car'].widget.attrs['readonly'] = True
        self.fields['Total_Payment'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True

    class Meta:
        model = Salesbooking
        fields = "__all__"
