# Generated by Django 3.2 on 2023-01-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20230126_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Rubric',
                'verbose_name_plural': 'Rubrics',
                'ordering': ['name'],
            },
        ),
    ]
