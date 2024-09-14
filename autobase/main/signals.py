from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Request, TaxPayment, StatisticsReport
from datetime import datetime

@receiver(post_save, sender=Request)
def create_tax_and_statistics(sender, instance, created, **kwargs):
    if created:
        # Создание записи о налоговом платеже
        tax_payment = TaxPayment.objects.create(
            request=instance,
            amount=instance.calculate_tax(),
            payment_date=datetime.now()
        )

        # Создание записи о статистическом отчете
        statistics_report = StatisticsReport.objects.create(
            request=instance,
            report_date=datetime.now(),
            report_file='path/to/report/file'  #  путь к отчету, если нада
        )
