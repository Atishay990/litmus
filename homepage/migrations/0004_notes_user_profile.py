# Generated by Django 3.0.3 on 2020-04-28 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('litmus', '0003_profile_email'),
        ('homepage', '0003_remove_notes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='user_profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='litmus.Profile'),
            preserve_default=False,
        ),
    ]