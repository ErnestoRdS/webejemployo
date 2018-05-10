# Generated by Django 2.0.4 on 2018-04-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['-created'], 'verbose_name': 'Portafolio', 'verbose_name_plural': 'Portafolios'},
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='elzelda',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='zelda'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='content',
            field=models.TextField(verbose_name='Relleno'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Primer dia'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='multimedia', verbose_name='Cuadro Magico'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulacho'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificacion'),
        ),
    ]
