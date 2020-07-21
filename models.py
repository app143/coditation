from django.db import models

class product(models.Model):
    name=models.CharField(max_length=9)
    brand=models.CharField(max_length=8)
    location=models.CharField(max_length=6)
    def __str__(self):
        return self.name



class category(models.Model):
    name=models.CharField(max_length=9)
    category_name=models.CharField(max_length=20)
    category_no=models.ForeignKey(product ,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class child_product(models.Model):
    child_product_name=models.CharField(max_length=20)
    child_product_no=models.ManyToManyField(category)
    def __str__(self):
        return self.name
# class category(models.Model):
#     category_name=models.CharField(max_length=20)
#     id=models.IntegerField()