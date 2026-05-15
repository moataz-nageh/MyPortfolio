"""
Views for the portfolio app.
"""

from django.shortcuts import render
from .models import (
    SiteConfig, Project, Certificate, Testimonial, SocialLink, Service,
    Education, Experience, Skill
)


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


def attach_project_tech_stack(projects):
    """Attach display-ready tech badge metadata without changing the database schema."""
    for project in projects:
        searchable_text = f'{project.title} {project.description}'.lower()
        project.tech_stack = [
            {'name': name, 'icon_class': icon_class}
            for name, icon_class, keywords in TECH_BADGE_DEFINITIONS
            if any(keyword in searchable_text for keyword in keywords)
        ]
    return projects


def index(request):
    """
    Main portfolio page view.
    Fetches all dynamic content and passes empty-state flags for template fallbacks.
    """
    # Fetch singleton config with defaults
    try:
        config = SiteConfig.objects.get(pk=1)
    except SiteConfig.DoesNotExist:
        config = None

    projects = attach_project_tech_stack(Project.objects.all())
    certificates = Certificate.objects.all()
    testimonials = Testimonial.objects.all()
    social_links = SocialLink.objects.all()
    services = Service.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()

    context = {
        'config': config,
        'projects': projects,
        'certificates': certificates,
        'testimonials': testimonials,
        'social_links': social_links,
        'services': services,
        'educations': educations,
        'experiences': experiences,
        'skills': skills,
        # Empty-state flags
        'has_projects': projects.exists(),
        'has_certificates': certificates.exists(),
        'has_testimonials': testimonials.exists(),
        'has_services': services.exists(),
        'has_social_links': social_links.exists(),
        'has_educations': educations.exists(),
        'has_experiences': experiences.exists(),
        'has_skills': skills.exists(),
        # SEO defaults when no config
        'site_title': config.site_title if config else 'Moataz Nageh Saber | AI Engineer Portfolio',
        'meta_description': config.meta_description if config else (
            'Portfolio of Moataz Nageh Saber — AI Engineer, '
            'and Data Analyst.'
        ),
    }
    return render(request, 'portfolio/index.html', context)
