from django.db import models
from django.utils import timezone

# Create your models here.
class articles(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return self.name

class customers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class orders(models.Model):
    time = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(articles, on_delete=models.CASCADE)
    customer = models.ForeignKey(customers, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.article}-{self.customer}"

