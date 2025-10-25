from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0036_update_repeating_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="date_format",
            field=models.CharField(
                choices=[("ymd", "YYYY-MM-DD"), ("dmy", "DD/MM/YYYY"), ("mdy", "MM/DD/YYYY")],
                default="ymd",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="time_format",
            field=models.CharField(
                choices=[("12", "12-hour"), ("24", "24-hour")],
                default="24",
                max_length=2,
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                name="date_format_valid",
                condition=models.Q(date_format__in=["ymd", "dmy", "mdy"]),
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                name="time_format_valid",
                condition=models.Q(time_format__in=["12", "24"]),
            ),
        ),
    ]
