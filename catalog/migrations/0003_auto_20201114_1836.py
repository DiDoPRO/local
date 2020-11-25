# Generated by Django 3.1.2 on 2020-11-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201114_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='borrower',
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Died'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1),
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
