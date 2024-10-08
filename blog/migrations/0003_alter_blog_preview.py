# Generated by Django 5.0.7 on 2024-09-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blog_preview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="preview",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото",
                null=True,
                upload_to="imgproduct/",
                verbose_name="Фото",
            ),
        ),
    ]
