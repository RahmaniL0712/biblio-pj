from django.db import migrations


def normalize_barcodes(apps, schema_editor):
    BookCopy = apps.get_model('core', 'BookCopy')
    database = schema_editor.connection.alias

    for number, copy in enumerate(
        BookCopy.objects.using(database).order_by('pk').iterator(),
        start=1,
    ):
        copy.barcode = f'BC{number:08d}'
        copy.save(using=database, update_fields=['barcode'])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_bookcopy_barcode'),
    ]

    operations = [
        migrations.RunPython(normalize_barcodes, migrations.RunPython.noop),
    ]