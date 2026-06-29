import django.db.models.deletion
from django.db import migrations, models


TECH_BADGE_DEFINITIONS = [
    ('Python', 'fa-brands fa-python', ('python',)),
    ('Django', 'fa-solid fa-code', ('django',)),
    ('Power BI', 'fa-solid fa-chart-pie', ('power bi', 'powerbi')),
    ('TensorFlow', 'fa-solid fa-brain', ('tensorflow', 'tensor flow')),
    ('PyTorch', 'fa-solid fa-fire', ('pytorch', 'torch')),
    ('BERT', 'fa-solid fa-language', ('bert',)),
    ('NLP', 'fa-solid fa-comments', ('nlp', 'sentiment')),
    ('OpenCV', 'fa-solid fa-eye', ('opencv', 'computer vision')),
    ('YOLOv8', 'fa-solid fa-crosshairs', ('yolov8', 'yolo')),
    ('TensorRT', 'fa-solid fa-microchip', ('tensorrt', 'edge deployment')),
    ('XGBoost', 'fa-solid fa-chart-line', ('xgboost',)),
    ('Flask', 'fa-solid fa-flask', ('flask',)),
    ('REST API', 'fa-solid fa-plug', ('rest api', 'api')),
    ('SQL', 'fa-solid fa-database', ('sql',)),
    ('Machine Learning', 'fa-solid fa-robot', ('machine learning', 'predict')),
    ('Data Analysis', 'fa-solid fa-magnifying-glass-chart', ('data analysis', 'dashboard')),
]


def migrate_inferred_project_tech_stack(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    ProjectTechStack = apps.get_model('portfolio', 'ProjectTechStack')
    tech_stack_items = []

    for project in Project.objects.all():
        searchable_text = f'{project.title} {project.description}'.lower()
        display_order = 0

        for name, icon_class, keywords in TECH_BADGE_DEFINITIONS:
            if any(keyword in searchable_text for keyword in keywords):
                tech_stack_items.append(
                    ProjectTechStack(
                        project_id=project.pk,
                        name=name,
                        icon_class=icon_class,
                        order=display_order,
                    )
                )
                display_order += 1

    ProjectTechStack.objects.bulk_create(tech_stack_items)


def remove_migrated_project_tech_stack(apps, schema_editor):
    ProjectTechStack = apps.get_model('portfolio', 'ProjectTechStack')
    ProjectTechStack.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_education_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTechStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon_class', models.CharField(help_text='Font Awesome class, e.g. "fa-brands fa-python"', max_length=100)),
                ('order', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech_stack', to='portfolio.project')),
            ],
            options={
                'verbose_name': 'Project tech stack item',
                'verbose_name_plural': 'Project tech stack items',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.RunPython(
            migrate_inferred_project_tech_stack,
            reverse_code=remove_migrated_project_tech_stack,
        ),
    ]
