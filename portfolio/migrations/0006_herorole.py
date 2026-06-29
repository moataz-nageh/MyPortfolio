from django.db import migrations, models


def seed_hero_roles(apps, schema_editor):
    HeroRole = apps.get_model('portfolio', 'HeroRole')
    if HeroRole.objects.exists():
        return

    HeroRole.objects.bulk_create([
        HeroRole(title='AI Engineer', display_order=0),
        HeroRole(title='Data Analyst', display_order=1),
    ])


def remove_seeded_hero_roles(apps, schema_editor):
    HeroRole = apps.get_model('portfolio', 'HeroRole')
    HeroRole.objects.filter(title__in=['AI Engineer', 'Data Analyst']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_projecttechstack'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Hero role',
                'verbose_name_plural': 'Hero roles',
                'ordering': ['display_order', 'id'],
            },
        ),
        migrations.RunPython(seed_hero_roles, reverse_code=remove_seeded_hero_roles),
    ]
