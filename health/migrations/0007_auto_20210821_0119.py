from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_search_data_craeted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search_data',
            name='craeted',
        ),
        migrations.AddField(
            model_name='search_data',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]














'''This is a Django database migration that removes a field called 'craeted' from the 'Search_Data' model
in the 'health' app, and adds a new field called 'created' of type DateTimeField with 'auto_now=True' 
option.
The 'auto_now=True' option sets the value of the field to the current date and time every time the model 
is saved.'''