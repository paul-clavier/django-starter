# Generated by Django 4.2.1 on 2023-05-09 16:25

import authentication.models.user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import django.utils.timezone
import secrets


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccessToken",
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
                (
                    "fingerprint",
                    authentication.models.user.FingerprintField(
                        editable=False, max_length=128
                    ),
                ),
                (
                    "token_id",
                    models.TextField(
                        default=authentication.models.user.generate_token_id,
                        editable=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmailValidationToken",
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
                ("token", models.TextField(default=secrets.token_urlsafe, unique=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="ResetPasswordToken",
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
                (
                    "token",
                    models.TextField(default=secrets.token_urlsafe, editable=False),
                ),
                (
                    "expiration_date",
                    models.DateTimeField(
                        default=authentication.models.user.one_hour_from_now,
                        editable=False,
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ["date_joined"]},
        ),
        migrations.AddField(
            model_name="user",
            name="last_read_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="user",
            name="verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=150, verbose_name="first name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=150, verbose_name="last name"),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("email"),
                name="unique_lowercase_user_email",
            ),
        ),
        migrations.AddField(
            model_name="resetpasswordtoken",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reset_password_token",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="emailvalidationtoken",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="email_validation_token",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="accesstoken",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="access_token",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
