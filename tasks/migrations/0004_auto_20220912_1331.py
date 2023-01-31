# Generated by Django 3.2.6 on 2022-09-12 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_corrector"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0003_add_level6"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="team",
        ),
        migrations.AddField(
            model_name="task",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tasks",
                to="accounts.team",
            ),
        ),
        migrations.AlterField(
            model_name="taskcomment",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]