from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_search_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.patient')),
            ],
        ),
    ]















'''This code is a Django migration file that creates a new model named "Feedback" with four fields: 
"messages", "date", "user", and "id".
The "messages" field is a TextField that can store a long string of text, and the "date" field is a 
DateField that can store a date. Both of these fields are allowed to be null.
The "user" field is a foreign key to the "patient" model in the "health" app, and has the attribute 
"on_delete=django.db.models.deletion.CASCADE", which means that if the related patient is deleted, all 
related feedback data will also be deleted.
The "id" field is an automatically generated primary key field for the Feedback model.
This migration file has a dependency on a previous migration file named "0003_search_data", which means 
that the previous migration file must be applied first before this migration file can be applied.
Once this migration is applied, the "Feedback" model will be available for use in the Django application,
 and instances of this model can be created to store feedback data related to a specific patient.






'''
