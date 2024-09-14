from django import forms
from .models import Request, TaxPayment, StatisticsReport, BusSchedule

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['client_name', 'request_type', 'route']
        widgets = {
            'request_type': forms.Select(choices=[('small', 'Small'), ('medium', 'Medium'), ('large','Дarge')]),
        }
class TaxPaymentForm(forms.ModelForm):
    class Meta:
        model = TaxPayment
        fields = ['request', 'amount', 'payment_date']

class StatisticsReportForm(forms.ModelForm):
    class Meta:
        model = StatisticsReport
        fields = ['request', 'report_date', 'report_file']


class BusScheduleForm(forms.ModelForm):
    class Meta:
        model = BusSchedule
        fields = ['bus_number', 'departure_time', 'arrival_time', 'route']