from django.db import models
import datetime

# Create your models here.

#Product table containing its metadata and its requirements
class Product(models.Model):
   
    item_name = models.CharField(max_length = 50, null=True, blank = True)
    total_quantity = models.PositiveIntegerField(default = 0, null = True, blank = False)
    issued_quantity = models.IntegerField(default = 0, null = True, blank = False)
    received_quantity = models.PositiveIntegerField(default = 0, null = True, blank = False)
    unit_price = models.PositiveIntegerField(default = 0, null = True, blank = False)

    def __str__(self):
        return self.item_name
  
#Sales table containing its metadata and its requirements
class Sale(models.Model):
    product = Product()
    format = '%a %d %B %Y %H:%M:%S'
    time = datetime.datetime.now()
    time_purchase = datetime.datetime.strftime(time, format)
    time_purchase_str = datetime.datetime.strptime(time_purchase, format)
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0, blank = False)
    amount_received = models.PositiveIntegerField(default = 0, null = True, blank = False)
    issued_to = models.CharField(max_length = 50, default = "Someone", blank = False)
    unit_price = models.PositiveIntegerField(default = 0, null = True, blank = False)
    date_of_purchase = models.CharField(default=time_purchase_str, max_length=255, null=True, blank=True )

    #returns the total of ordered quantity
    def get_total(self):
            total = self.quantity * self.item.unit_price
            return float(total)
        
    #returns the difference between the amount received and the total cost of order
    def get_change(self):
            change = self.amount_received - self.get_total()
            
            return float(change)
            
    
    def __str__(self):
        return self.item.item_name
