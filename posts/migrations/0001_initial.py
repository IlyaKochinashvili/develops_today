# Generated by Django 3.0.6 on 2020-05-21 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=256, unique=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('amount_of_upvotes', models.PositiveIntegerField(default=0)),
                ('author_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
    ]
