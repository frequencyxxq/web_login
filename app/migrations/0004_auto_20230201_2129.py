# Generated by Django 2.2.25 on 2023-02-01 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230129_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuesubcategory',
            name='issue_categoty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_subcategories', to='app.IssueCategory'),
        ),
    ]
