# Generated by Django 2.1.7 on 2020-04-16 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Owners_HR',
        ),
        migrations.AlterField(
            model_name='comment',
            name='Addressed_Book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Books'),
        ),
    ]