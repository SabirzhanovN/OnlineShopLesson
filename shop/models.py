from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    date_of_create = models.DateTimeField(auto_now=True)

    main_image = models.ImageField(upload_to="Photos")
    image_1 = models.ImageField(upload_to="Photos", null=True, blank=True)
    image_2 = models.ImageField(upload_to="Photos", null=True, blank=True)
    image_3 = models.ImageField(upload_to="Photos", null=True, blank=True)

    CATALOGS = (
        (1, "Men"),
        (2, "Women")
    )
    catalog = models.IntegerField(choices=CATALOGS)

    def __str__(self):
        return self.name
