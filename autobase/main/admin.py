from django.contrib import admin
from .models import Request, TaxPayment, StatisticsReport, BusSchedule

class BusScheduleAdmin(admin.ModelAdmin):
    list_display = ('bus_number', 'departure_time', 'arrival_time', 'route')
    search_fields = ('bus_number', 'route')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'request_type', 'route', 'status', 'created_at')
    search_fields = ('client_name', 'request_type', 'status')

class TaxPaymentAdmin(admin.ModelAdmin):
    list_display = ('request', 'amount', 'payment_date')
    search_fields = ('request__client_name', 'amount')
    list_filter = ('payment_date',)

class StatisticsReportAdmin(admin.ModelAdmin):
    list_display = ('request', 'report_date', 'report_file')
    search_fields = ('request__client_name',)
    list_filter = ('report_date',)

admin.site.register(Request, RequestAdmin)
admin.site.register(TaxPayment, TaxPaymentAdmin)
admin.site.register(StatisticsReport, StatisticsReportAdmin)
admin.site.register(BusSchedule, BusScheduleAdmin)