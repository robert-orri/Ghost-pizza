# Generated by Django 4.2.1 on 2023-05-11 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ghost', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manufacturer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacturer.offer')),
                ('pizza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ghost.pizza')),
            ],
        ),
    ]
