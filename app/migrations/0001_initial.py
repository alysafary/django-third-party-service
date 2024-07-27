# Generated by Django 5.0.7 on 2024-07-27 17:11

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ApiKeyScope",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="ApiKeyScopeView",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("url", models.CharField(max_length=128)),
                ("regex", models.TextField(verbose_name="regex")),
            ],
        ),
        migrations.CreateModel(
            name="AccessApiKey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=128, null=True)),
                ("key", models.CharField(max_length=64, unique=True)),
                ("is_enable", models.BooleanField(default=True)),
                (
                    "whitelisted_ips",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.GenericIPAddressField(
                            validators=[django.core.validators.validate_ipv46_address]
                        ),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                ("scopes", models.ManyToManyField(to="app.apikeyscope")),
            ],
        ),
        migrations.AddField(
            model_name="apikeyscope",
            name="views",
            field=models.ManyToManyField(to="app.apikeyscopeview"),
        ),
    ]
