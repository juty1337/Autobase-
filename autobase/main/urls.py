from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create-request/', views.create_request, name='create_request'),
    path('success/', views.success, name='success'),
    path('requests/', views.request_list, name='request_list'),
    path('create-schedule/', views.create_schedule, name='create_schedule'),
    path('create-tax-payment/', views.create_tax_payment, name='create_tax_payment'),
    path('tax-payment-success/', views.tax_payment_success, name='tax_payment_success'),
    path('tax-payments/', views.tax_payment_list, name='tax_payment_list'),
    path('create-statistics-report/', views.create_statistics_report, name='create_statistics_report'),
    path('statistics-report-success/', views.statistics_report_success, name='statistics_report_success'),
    path('statistics-reports/', views.statistics_report_list, name='statistics_report_list'),
]