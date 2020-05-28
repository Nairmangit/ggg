# Generated by Django 3.0.2 on 2020-04-29 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='obj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Э', 'Электроэнергия'), ('ХВ', 'Холодная вода'), ('ГВ', 'Горячая вода')], max_length=2)),
                ('objfk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grr.obj')),
            ],
        ),
        migrations.CreateModel(
            name='values_sens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tem', models.DecimalField(decimal_places=4, max_digits=11)),
                ('dat', models.DateTimeField()),
                ('sensfk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grr.sens')),
            ],
        ),
    ]
