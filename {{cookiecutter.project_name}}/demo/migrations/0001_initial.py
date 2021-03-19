# Generated by Django 2.2.14 on 2021-01-02 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=10, verbose_name='a')),
            ],
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b', models.CharField(max_length=10, verbose_name='b')),
            ],
        ),
        migrations.CreateModel(
            name='AB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c', models.CharField(max_length=10, verbose_name='c')),
                ('a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.A')),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.B')),
            ],
        ),
        migrations.AddField(
            model_name='a',
            name='m2m',
            field=models.ManyToManyField(through='demo.AB', to='demo.B'),
        ),
    ]
