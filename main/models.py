from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# landing page model
class ProductModel(models.Model):
    product = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='pimages', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.product