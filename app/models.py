from django.db import models


# Create your models here.
class Debt(models.Model):
    debtor_name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    data_created = models.DateTimeField(auto_now_add=True)
    data_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.debtor_name} - {self.amount} сом - {self.description})"

