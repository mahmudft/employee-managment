# Generated by Django 4.1.1 on 2022-10-02 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_teamleader_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="team",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api.team",
            ),
        ),
    ]
