# Generated by Django 4.2.6 on 2023-11-01 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hair', models.BooleanField(default=False)),
                ('eyebrow', models.BooleanField(default=False)),
                ('beard', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
