# Generated by Django 4.1 on 2022-08-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fit",
            name="ingredients",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="fit",
            name="kcal",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="fit",
            name="photo",
            field=models.ImageField(
                default="media/food.svg", upload_to="uploaded_media"
            ),
        ),
    ]
