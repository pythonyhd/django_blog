# Generated by Django 2.2.6 on 2019-12-02 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(help_text='编号决定图片播放的顺序，图片不要多于5张', verbose_name='编号')),
                ('title', models.CharField(blank=True, help_text='标题可以为空', max_length=20, null=True, verbose_name='标题')),
                ('content', models.CharField(max_length=80, verbose_name='描述')),
                ('img_url', models.CharField(max_length=200, verbose_name='图片地址')),
                ('url', models.CharField(default='#', help_text='图片跳转的超链接，默认#表示不跳转', max_length=200, verbose_name='跳转链接')),
            ],
            options={
                'verbose_name': '图片轮播',
                'verbose_name_plural': '图片轮播',
                'ordering': ['number', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='文章类型')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('source_id', models.CharField(max_length=25, verbose_name='文章id或source名称')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='评论时间')),
                ('user_name', models.CharField(max_length=25, verbose_name='评论用户')),
                ('url', models.CharField(max_length=100, verbose_name='链接')),
                ('comment', models.CharField(max_length=500, verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='网站名称')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='网站描述')),
                ('link', models.URLField(help_text='请填写http或https开头的完整形式地址', verbose_name='友链地址')),
                ('logo', models.URLField(blank=True, help_text='请填写http或https开头的完整形式地址', verbose_name='网站LOGO')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否首页展示')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_time', models.DateField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('digest', models.TextField(blank=True, null=True)),
                ('view', models.BigIntegerField(default=0)),
                ('comment', models.BigIntegerField(default=0)),
                ('picture', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='文章类型')),
                ('tag', models.ManyToManyField(to='blog.Tag')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-create_date'],
            },
        ),
    ]