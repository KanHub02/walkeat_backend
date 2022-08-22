from django.db import models


categories_choice = (
    ("sets", "sets"),
    ("lunch", "lunch"),
    ("breakfast", "breakfast"),
    ("dinner", "dinner"),
    ("salad", "salad"),
    ("drink", "drink"),
)

week_choices = (
    ("monday", "monday"),
    ("tuesday", "tuesday"),
    ("wednesday", "wednesday"),
    ("thursday", "thursday"),
    ("friday", "friday"),
    ("saturday", "saturday"),
    ("sunday", "sunday"),
)


class Category(models.Model):
    category = models.CharField(choices=categories_choice, max_length=255, unique=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Fit(models.Model):
    photo = models.ImageField(default="media/food.svg", upload_to="uploaded_media")
    title = models.CharField(max_length=35)
    calories = models.FloatField(default=0.0)
    carbohydrates = models.FloatField(default=0.0)
    protein = models.FloatField(default=0.0)
    fats = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    ingredients = models.CharField(max_length=255)
    kcal = models.FloatField(default=0.0)
    category = models.ManyToManyField(Category, related_name="categories")

    def __str__(self):
        return self.title


# Create your models here.
