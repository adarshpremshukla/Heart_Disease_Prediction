from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health', '0004_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]















'''This is a Django migration file that alters the Feedback model in the health app.
It has two dependencies: settings.AUTH_USER_MODEL and the previous migration health.0004_feedback.
The migration performs two AlterField operations on the Feedback model. It changes the date field to 
automatically set the current date using auto_now=True, and it changes the user field to a foreign key 
to settings.AUTH_USER_MODEL.'''