# Generated by Django 2.0.1 on 2018-02-17 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adress_book', '0010_contactinfo_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]