# Generated by Django 4.1 on 2024-10-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="job",
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
                ("title", models.CharField(max_length=20)),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("FULL TIME", "FULL TIME "),
                            ("PART TIME", "PART TIME "),
                        ],
                        max_length=20,
                    ),
                ),
                ("description", models.TextField(max_length=1200)),
                ("published_at", models.DateTimeField(auto_now_add=True)),
                ("Vacancy", models.IntegerField(default=1, max_length=10)),
                ("salary", models.IntegerField(default=300, max_length=10)),
                ("experiences", models.IntegerField(default=0, max_length=10)),
            ],
        ),
    ]