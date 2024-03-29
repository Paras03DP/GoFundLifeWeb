import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='age',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='disease',
        ),
        migrations.CreateModel(
            name='BloodDonate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(default='Nothing', max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.Donor')),
            ],
        ),
    ]
