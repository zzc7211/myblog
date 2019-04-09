# Generated by Django 2.1.7 on 2019-04-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='在这里写作品的简介', max_length=100)),
                ('image', models.ImageField(default='default.png', upload_to='images/')),
                ('title', models.CharField(default='作品标题', max_length=50)),
            ],
        ),
    ]
