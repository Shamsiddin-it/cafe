from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField( upload_to="static/images/category",null=True, blank=True)
    def __str__(self):
        return self.name

class Dish(models.Model):
    image = models.ImageField(upload_to="static/images/dish")
    name = models.CharField( max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.CharField( max_length=50)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name
    class Meta:
        default_permissions = ('view') 
        permissions = (
            ('add_dish', 'Can add dish'),
            ('change_dish', 'Can change dish'),
            ('del_dish', 'Can del dish'),
        )

class Staf(models.Model):
    image = models.ImageField(upload_to="static/images/staf")
    name = models.CharField( max_length=150)
    age = models.IntegerField()
    phone = models.CharField(max_length=13)    
    def __str__(self):
        return self.name
    class Meta:
        default_permissions = ('view') 
        permissions = (
            ('add_staf', 'Can add staf'),
            ('change_staf', 'Can change staf'),
            ('del_staf', 'Can del staf'),
        )
