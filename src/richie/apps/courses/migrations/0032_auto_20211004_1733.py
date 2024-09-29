# Generated by Django 3.2.7 on 2021-10-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0031_auto_20210811_1234"),
    ]

    operations = [
        migrations.AddField(
            model_name="courserun",
            name="enrollment_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="The number of enrolled students",
                verbose_name="enrollment count",
            ),
        ),
    ]
