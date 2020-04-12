# Generated by Django 2.1.7 on 2020-04-12 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('books', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('items', models.ManyToManyField(to='books.Proposed_Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='Users.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='owner_want_to_buy',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ref_code',
        ),
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='Users.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='books.Proposed_Book'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.Cart'),
        ),
    ]
