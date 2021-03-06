# Generated by Django 2.2.6 on 2019-12-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-create_date'], 'verbose_name': '文章内容', 'verbose_name_plural': '文章内容'},
        ),
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['number', '-id'], 'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': '文章分类', 'verbose_name_plural': '文章分类'},
        ),
        migrations.AlterField(
            model_name='article',
            name='comment',
            field=models.BigIntegerField(default=0, verbose_name='评论数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='文章正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateField(auto_now_add=True, verbose_name='博客日期'),
        ),
        migrations.AlterField(
            model_name='article',
            name='digest',
            field=models.TextField(blank=True, null=True, verbose_name='文章摘要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.CharField(max_length=200, verbose_name='标题图片地址'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='view',
            field=models.BigIntegerField(default=0, verbose_name='阅读数'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=30, verbose_name='标签名称'),
        ),
    ]
