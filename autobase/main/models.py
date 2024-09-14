from django.db import models

class Request(models.Model):
    client_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=50, choices=[('small', 'Small'), ('medium', 'Medium'), ('large','Large')])

    
    route = models.TextField()
    
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client_name} - {self.request_type} - {self.status}'

    def calculate_tax(self):
      
        base_rate = 350 
        if self.request_type == 'small':
            return base_rate * 1.2 
        if self.request_type == 'medium':
            return base_rate * 1.5  
        if self.request_type == 'large':
            return base_rate * 2  
        else:
            return base_rate 

class TaxPayment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()

    def __str__(self):
        return f'Tax Payment for {self.request.client_name} - {self.amount}'

class StatisticsReport(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    report_date = models.DateTimeField()
    report_file = models.FileField(upload_to='reports/')

    def __str__(self):
        return f'Statistics Report for {self.request.client_name} - {self.report_date}'
    
class BusSchedule(models.Model):
    bus_number = models.CharField(max_length=10)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    route = models.TextField()

    def __str__(self):
        return f'Bus {self.bus_number} - {self.route}'