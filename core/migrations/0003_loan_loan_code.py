from django.db import migrations, models


def populate_loan_codes(apps, schema_editor):
    Loan = apps.get_model("core", "Loan")
    database = schema_editor.connection.alias

    for loan in Loan.objects.using(database).order_by("pk").iterator():
        loan.loan_code = f"L{loan.pk:09d}"
        loan.save(update_fields=["loan_code"])


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_book_isbn"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="loan_code",
            field=models.CharField(default="", max_length=10),
            preserve_default=False,
        ),
        migrations.RunPython(populate_loan_codes, migrations.RunPython.noop),
    ]