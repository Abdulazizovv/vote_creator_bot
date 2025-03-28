# Generated by Django 5.0.1 on 2025-02-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0004_voteoptionitem_voteoption_votepost_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='votepost',
            name='message_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'post')},
        ),
    ]
