# Generated by Django 4.1 on 2022-08-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_tools_toolstopics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Tile'),
        ),
    ]