# Generated by Django 2.2.2 on 2021-11-25 03:51

import ckeditor.fields
from django.db import migrations, models
import my_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20211124_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_tag', models.CharField(max_length=125)),
                ('author', models.CharField(max_length=125)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_pics', validators=[my_app.validators.image_validator])),
            ],
        ),
    ]
