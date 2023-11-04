import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_auto_20210818_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_data',
            name='craeted',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 8, 21, 0, 48, 4, 16823)),
            preserve_default=False,
        ),
    ]











'''
This is a Django database migration file that adds a new field named 'created' to the 'Search_Data' 
model in the 'health' app. The new field is a DateTimeField with auto_now_add=True option, which means 
that the current date and time will be automatically added to the field when a new 'Search_Data' object 
is created. The default value for the field is set to a specific date and time using the datetime module.
This migration file was generated on August 20, 2021, and depends on a previous migration file 
'0005_auto_20210818_2220'.'''