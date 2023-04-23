# Generated by Django 4.1.5 on 2023-04-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softwares', '0007_alter_software_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='so',
            field=models.CharField(choices=[('LI', 'Linux'), ('W0', 'MS Windows')], default='LI', max_length=2),
        ),
    ]
