# Generated by Django 2.1.4 on 2019-07-24 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datacatalog', '0012_auto_20190724_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_creation', models.DateField(auto_now_add=True)),
                ('record_update', models.DateField(auto_now=True)),
                ('name', models.CharField(help_text='The name of the field as it appears in schema', max_length=256)),
                ('description', models.CharField(help_text='Description of the field', max_length=256, unique=True)),
                ('scope', models.CharField(help_text='Descriptions of the scope of the data (eg. min, max, number of records, number of null values, number of unique values)', max_length=256)),
                ('record_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='data_fields',
        ),
        migrations.AlterField(
            model_name='dataset',
            name='record_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dataset',
            name='data_fields',
            field=models.ManyToManyField(blank=True, help_text='list of fields present in schema', to='datacatalog.DataField'),
        ),
    ]
