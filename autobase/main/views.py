from django.shortcuts import render, redirect
from .models import Request, TaxPayment, StatisticsReport, BusSchedule
from .forms import RequestForm, TaxPaymentForm, StatisticsReportForm, BusScheduleForm

def home(request):
    schedules = BusSchedule.objects.all()
    return render(request, 'main/home.html', {'schedules': schedules})


def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RequestForm()
    return render(request, 'main/create_request.html', {'form': form})


def success(request):
    return render(request, 'main/success.html')


def request_list(request):
    requests = Request.objects.all()
    return render(request, 'main/request_list.html', {'requests': requests})

def create_schedule(request):
    if request.method == 'POST':
        form = BusScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BusScheduleForm()
    return render(request, 'main/create_schedule.html', {'form': form})

def create_tax_payment(request):
    if request.method == 'POST':
        form = TaxPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tax_payment_success')
    else:
        form = TaxPaymentForm()
    return render(request, 'main/create_tax_payment.html', {'form': form})

def tax_payment_success(request):
    return render(request, 'main/tax_payment_success.html')

def tax_payment_list(request):
    tax_payments = TaxPayment.objects.all()
    return render(request, 'main/tax_payment_list.html', {'tax_payments': tax_payments})

def create_statistics_report(request):
    if request.method == 'POST':
        form = StatisticsReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('statistics_report_success')
    else:
        form = StatisticsReportForm()
    return render(request, 'main/create_statistics_report.html', {'form': form})

def statistics_report_success(request):
    return render(request, 'main/statistics_report_success.html')

def statistics_report_list(request):
    reports = StatisticsReport.objects.all()
    return render(request, 'main/statistics_report_list.html', {'reports': reports})