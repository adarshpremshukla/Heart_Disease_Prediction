from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(null=True, verbose_name=((1, 'Authorize'), (2, 'UnAuthorize')))),
                #modified
                # status , models.IntegerField(choices=((1, 'Authorized'), (2, 'Unauthorized')), null=True, verbose_name='Status'),
                ('contact', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('doj', models.DateField(null=True)),
                ('dob', models.DateField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]














'''This code is a Django migration file, which defines the changes to be made to the database schema.
Specifically, it creates two new models, "Patient" and "Doctor", which both have several fields such as
"contact", "address", "dob" (date of birth), "image", and a foreign key to the Django User model 
(settings.AUTH_USER_MODEL).
For the "Doctor" model, the original "status" field has been modified to use the "choices" attribute to
restrict the field to two possible values: "Authorized" and "Unauthorized". The "Doctor" model also has
a "category" field.
These changes will be applied to the database when the migration is run using the Django migration 
commands.'''