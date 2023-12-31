# Generated by Django 4.2.4 on 2023-08-11 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import home.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_alter_profile_biografia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=home.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.CharField(max_length=100)),
                ('image', models.ManyToManyField(blank=True, to='home.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ImagePosts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
