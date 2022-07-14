# Generated by Django 4.0.5 on 2022-07-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True)),
                ('genre', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
