# Generated by Django 4.0.5 on 2022-06-20 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodwatch', '0003_alter_neighbourhood_logo_alter_profile_neighbourhood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='logo',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_logo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
