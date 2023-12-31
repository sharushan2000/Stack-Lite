# Generated by Django 4.2 on 2023-11-14 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('describe', models.TextField(max_length=500)),
                ('code', models.TextField(max_length=1500)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('github', models.URLField(blank=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type', to='learn_app.contenttype')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
