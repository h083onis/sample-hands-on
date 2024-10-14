from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0002_category"),
    ]

    operations = [
        migrations.RunSQL(
            "INSERT INTO category( name, parent_category_id ) VALUES( 'メンズ', null );",
        )
    ]