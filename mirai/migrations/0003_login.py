# Generated by Django 3.0.7 on 2022-02-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirai', '0002_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]
