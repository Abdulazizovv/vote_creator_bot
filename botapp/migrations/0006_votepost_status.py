# Generated by Django 5.0.1 on 2025-02-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0005_votepost_message_id_alter_vote_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='votepost',
            name='status',
            field=models.CharField(default='draft', max_length=15),
        ),
    ]
