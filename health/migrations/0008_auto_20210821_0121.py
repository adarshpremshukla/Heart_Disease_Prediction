from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0007_auto_20210821_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_data',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]













'''This Django migration changes the field created of the Search_Data model in the health app. It 
modifies the field to be nullable by setting null=True and keeps the auto_now feature to update the 
field with the current timestamp on every save.'''