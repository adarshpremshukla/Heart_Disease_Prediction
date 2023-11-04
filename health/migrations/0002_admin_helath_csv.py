from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name="Admin_Helath_CSV",
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('csv_file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]









    
'''This is a Django migration file that creates a new model named "Admin_Helath_CSV" with two fields:
"name" and "csv_file". The "name" field is a CharField that can store a string of up to 100 characters, 
and the "csv_file" field is a FileField that can store an uploaded file.
The "csv_file" field has the optional attribute "blank=True", which allows the field to be empty. The 
"csv_file" field also has the attribute "upload_to=''", which means the uploaded file will be saved to
the root directory of the media folder.
This migration file has a dependency on a previous migration file named "0001_initial", which means that 
the previous migration file must be applied first before this migration file can be applied.
Once this migration is applied, the "Admin_Helath_CSV" model will be available for use in the Django 
application, and instances of this model can be created to store information about uploaded CSV files.'''