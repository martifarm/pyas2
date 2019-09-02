# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyas2', '0023_auto_20190902_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='as2_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='AS2 Identifier'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Organization Name'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='as2_name',
            field=models.CharField(max_length=100, verbose_name='AS2 Identifier'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='extra_headers',
            field=models.TextField(blank=True, null=True, verbose_name='Extra Headers'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Partner Name'),
        ),
    ]
