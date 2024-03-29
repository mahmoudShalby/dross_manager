# Generated by Django 4.0.3 on 2023-04-18 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('classes', models.PositiveSmallIntegerField(default=0)),
                ('class_price', models.PositiveSmallIntegerField()),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.grade')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('egp', models.PositiveSmallIntegerField(default=0)),
                ('paid', models.PositiveSmallIntegerField(default=0)),
                ('attendance', models.PositiveSmallIntegerField(default=0)),
                ('have_to_pay', models.BooleanField(default=True)),
                ('level', models.TextField(choices=[('N', 'Normal'), ('I', 'Intermediate'), ('A', 'Advanced')], default='N', max_length=1)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.group')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('max_mark', models.PositiveSmallIntegerField()),
                ('level', models.CharField(choices=[('A', 'Any'), ('E', 'Ease'), ('M', 'Middle'), ('H', 'Hard')], default='A', max_length=1)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('takers', models.ManyToManyField(to='core.student')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stage'),
        ),
    ]
