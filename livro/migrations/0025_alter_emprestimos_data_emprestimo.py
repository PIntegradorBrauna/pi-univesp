# Generated by Django 4.1.2 on 2022-11-09 02:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0024_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 8, 23, 11, 28, 738795)),
        ),
    ]
