"""
Views for the portfolio app.
"""

from django.shortcuts import render
from .models import (
    SiteConfig, Project, Certificate, Testimonial, SocialLink, Service,
    Education, Experience, Skill
)


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

    projects = Project.objects.all()
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
