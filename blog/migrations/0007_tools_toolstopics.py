# Generated by Django 4.1 on 2022-08-27 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_details_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool', models.CharField(max_length=50, verbose_name='Tool')),
                ('title', models.CharField(max_length=50, verbose_name='Tile')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='ToolsTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tile')),
                ('year', models.DateField(auto_now=True)),
                ('description', models.CharField(max_length=120, verbose_name='Description')),
                ('idToll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tools')),
            ],
        ),
    ]
