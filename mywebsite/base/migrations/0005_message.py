# Generated by Django 4.2.14 on 2024-07-24 18:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_skill_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
