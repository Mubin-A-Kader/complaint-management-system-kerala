# Generated by Django 4.0.5 on 2022-06-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0013_alter_mechanic_work_category_mechanic2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mechanic2',
            name='salary',
        ),
        migrations.AddField(
            model_name='mechanic2',
            name='district',
            field=models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Wayanad', 'Wayanad'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Pathanamthitta', 'Pathanamthitta'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Kottayam', 'Kottayam'), ('Kollam', 'Kollam'), ('Kasaragod', 'Kasaragod'), ('Kannur', 'Kannur'), ('Idukki', 'Idukki')], default='alappuzha', max_length=50),
            preserve_default=False,
        ),
    ]