# Generated by Django 4.2.23 on 2025-07-04 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0004_topicmodel_created_topicmodel_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rommodel',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterModelOptions(
            name='topicmodel',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='rom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roommessages+', to='myapp.rommodel'),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usermessages+', to=settings.AUTH_USER_MODEL),
        ),
    ]
