from django.db import models


class Address(models.Model):
    """não pensei muito na hora de modelar o endereço.
    em algum outro momento eu penso melhor.
    é só um mvp.
    """

    class Meta:
        verbose_name_plural = "addresses"

    postal_code = models.CharField(max_length=10)
    street_name = models.CharField(max_length=50, null=True, default=None)
    street_number = models.IntegerField(null=True)
    store_number = models.IntegerField(null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)


class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.ForeignKey(
        Address, default=None, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Place - {self.name}"
