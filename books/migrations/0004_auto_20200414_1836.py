# Generated by Django 2.1.7 on 2020-04-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200414_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposed_book',
            name='Proposed_book',
        ),
        migrations.AddField(
            model_name='proposed_book',
            name='Proposed_book',
            field=models.ManyToManyField(to='books.Books'),
        ),
    ]