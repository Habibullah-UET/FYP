#  Habibullah
#  @ Dragunov
#  Unixian@outlook.com  
#  4/12/2016

from django.db import models

# Database Table structure of Products

class Product (models.Model) :
    Product_Title = models.CharField( max_length= 200 )
    Product_Image = models.CharField( max_length=100  )
    Product_Description = models.CharField( max_length = 500  )
    Product_Price = models.CharField(max_length= 5)
    Product_Rating = models.CharField(max_length=3)
    Product_Stock  = models.CharField( max_length = 5 , blank = True)

    def __str__(self) :
        return self.Product_Title
