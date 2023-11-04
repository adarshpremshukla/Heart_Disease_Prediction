from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_admin_helath_csv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction_accuracy', models.CharField(blank=True, max_length=100, null=True)),
                ('result', models.CharField(blank=True, max_length=100, null=True)),
                ('values_list', models.CharField(blank=True, max_length=100, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.patient')),
            ],
        ),
    ]













'''
This code is a Django migration file that creates a new model named "Search_Data" with four fields: 
"prediction_accuracy", "result", "values_list", and "patient".
The "prediction_accuracy" field is a CharField that can store a string of up to 100 characters, and the 
"result" and "values_list" fields are also CharFields that can store strings of up to 100 characters, but
these fields are allowed to be empty or null.
The "patient" field is a foreign key to the "patient" model in the "health" app, and has the attribute 
"on_delete=django.db.models.deletion.CASCADE", which means that if the related patient is deleted, all 
related search data will also be deleted.
This migration file has a dependency on a previous migration file named "0002_admin_helath_csv", which 
means that the previous migration file must be applied first before this migration file can be applied.
Once this migration is applied, the "Search_Data" model will be available for use in the Django 
application, and instances of this model can be created to store search data related to a specific
patient.'''