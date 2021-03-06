# Generated by Django 2.0.13 on 2019-04-10 19:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('codigo', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Preço')),
                ('imagem', models.FileField(blank=True, null=True, upload_to='produtos/')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='TipoProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tipo do produto',
                'verbose_name_plural': 'Tipos do produto',
            },
        ),
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.TipoProduto'),
        ),
    ]
