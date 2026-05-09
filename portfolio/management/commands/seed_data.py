import inspect
from django.core.management.base import BaseCommand
from portfolio.models import (
    SiteConfig, Project, Certificate, Testimonial, SocialLink, Service,
    Education, Experience, Skill
)


class Command(BaseCommand):
    help = 'Seed the database with sample portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # --- Site Configuration ---
        SiteConfig.objects.update_or_create(pk=1, defaults={
            'site_title': 'Moataz Nageh Saber | AI Engineer Portfolio',
            'meta_description': (
                'Portfolio of Moataz Nageh Saber — AI Engineer, '
                'and Data Analyst. Explore projects, skills, and experience.'
            ),
            'name': 'Moataz Nageh Saber',
            'hero_description': 'Transforming data into intelligent solutions through Machine Learning, AI, and advanced analytics.',
            'about_me': (
                'Machine Learning–focused Data Scientist with strong expertise in building, evaluating, and deploying '
                'data-driven models. Experienced in machine learning, artificial intelligence, and data analysis to '
                'solve real-world problems through predictive modeling and statistical techniques. Skilled in extracting '
                'actionable insights from complex datasets to support data-informed decision-making and deliver scalable, '
                'high-impact solutions.'
            ),
            'cv_link': 'https://drive.google.com/your-cv-link-here'
        })
        self.stdout.write(self.style.SUCCESS('  [OK] SiteConfig'))

        # --- Projects ---
        projects = [
            {
                'title': 'Sentiment Analysis NLP Pipeline',
                'description': 'Built an end-to-end NLP pipeline for sentiment analysis on product reviews using BERT and TensorFlow. Achieved 94% accuracy on the test set with custom preprocessing and fine-tuning.',
                'github_link': 'https://github.com/',
                'order': 1,
            },
            {
                'title': 'Real-Time Object Detection System',
                'description': 'Developed a real-time object detection application using YOLOv8 and OpenCV. Optimized for edge deployment with TensorRT, achieving 30+ FPS on embedded hardware.',
                'github_link': 'https://github.com/',
                'order': 2,
            },
            {
                'title': 'Customer Churn Prediction',
                'description': 'Created a machine learning model to predict customer churn using XGBoost and feature engineering. Deployed as a REST API with Flask, reducing churn by 15%.',
                'github_link': 'https://github.com/',
                'order': 3,
            },
        ]
        for p in projects:
            Project.objects.update_or_create(title=p['title'], defaults=p)
        self.stdout.write(self.style.SUCCESS(f'  [OK] {len(projects)} Projects'))

        # --- Certificates ---
        certificates = [
            {
                'title': 'Machine Learning Specialization',
                'issuer': 'Stanford Online (Coursera)',
                'date': '2024',
                'link': 'https://drive.google.com/',
                'order': 1,
            },
            {
                'title': 'Deep Learning Specialization',
                'issuer': 'DeepLearning.AI (Coursera)',
                'date': '2024',
                'link': 'https://drive.google.com/',
                'order': 2,
            },
        ]
        for c in certificates:
            Certificate.objects.update_or_create(title=c['title'], defaults=c)
        self.stdout.write(self.style.SUCCESS(f'  [OK] {len(certificates)} Certificates'))

        # --- Testimonials ---
        testimonials = [
            {
                'name': 'Ahmed Hassan',
                'review': 'Moataz delivered an outstanding ML model that exceeded our expectations. His attention to detail and deep understanding of data science made the project a huge success.',
                'rating': 5,
                'order': 1,
            },
        ]
        for t in testimonials:
            Testimonial.objects.update_or_create(name=t['name'], defaults=t)
        self.stdout.write(self.style.SUCCESS(f'  [OK] {len(testimonials)} Testimonials'))

        # --- Social Links ---
        social_links = [
            {
                'platform': 'linkedin',
                'url': 'https://www.linkedin.com/in/moatazn/',
                'icon_class': 'fa-brands fa-linkedin',
                'order': 1,
            },
            {
                'platform': 'github',
                'url': 'https://github.com/',
                'icon_class': 'fa-brands fa-github',
                'order': 2,
            },
        ]
        for s in social_links:
            SocialLink.objects.update_or_create(platform=s['platform'], defaults=s)
        self.stdout.write(self.style.SUCCESS(f'  [OK] {len(social_links)} Social Links'))

        # --- Services ---
        services = [
            {
                'title': 'Machine Learning Solutions',
                'description': 'Design, develop, and deploy custom machine learning models tailored to your business needs — from classification to regression and clustering.',
                'icon_class': 'fa-solid fa-brain',
                'order': 1,
            },
        ]
        for s in services:
            Service.objects.update_or_create(title=s['title'], defaults=s)
        self.stdout.write(self.style.SUCCESS(f'  [OK] {len(services)} Services'))

        # --- Education ---
        educations = [
            {
                'degree': "Bachelor's Degree in Computer Science",
                'specialization': "Specializing in Data Science and Artificial Intelligence",
                'university': "Canadian International College (CIC)",
                'order': 1,
            }
        ]
        for e in educations:
            Education.objects.update_or_create(degree=e['degree'], university=e['university'], defaults=e)
        self.stdout.write(self.style.SUCCESS(f'  [OK] {len(educations)} Education records'))

        # --- Experience ---
        experiences = [
            {
                'title': 'Machine Learning Intern',
                'company': 'CodeAlpha',
                'start_date': 'Jun 2025',
                'end_date': 'Jul 2025',
                'description': 'Worked on data preprocessing and feature engineering for machine learning projects. Developed and trained ML models using Python, scikit-learn, TensorFlow.',
                'icon_class': 'fa-solid fa-building',
                'order': 1,
            },
            {
                'title': 'DEPI AI & Data Science Trainee',
                'company': 'DEPI',
                'start_date': 'Oct 2024',
                'end_date': 'May 2025',
                'description': 'Focused on applied machine learning and data-driven problem solving.',
                'icon_class': 'fa-solid fa-building',
                'order': 2,
            },
            {
                'title': 'ECPC Participant',
                'company': 'ECPC',
                'start_date': '2024',
                'end_date': '2024',
                'description': 'Solved competitive programming challenges in a team environment.',
                'icon_class': 'fa-solid fa-trophy',
                'order': 3,
            },
            {
                'title': 'Flutter Track Lead',
                'company': 'GDG on Campus CIC',
                'start_date': 'Nov 2024',
                'end_date': 'Sep 2025',
                'description': 'Led a Flutter team, mentoring developers and building apps.',
                'icon_class': 'fa-solid fa-building',
                'order': 4,
            },
        ]
        for ex in experiences:
            Experience.objects.update_or_create(title=ex['title'], company=ex['company'], defaults=ex)
        self.stdout.write(self.style.SUCCESS(f'  [OK] {len(experiences)} Experience records'))

        # --- Skills ---
        skills = [
            {'name': 'Python', 'icon_class': 'fa-brands fa-python', 'order': 1},
            {'name': 'SQL', 'icon_class': 'fa-solid fa-database', 'order': 2},
            {'name': 'Git & GitHub', 'icon_class': 'fa-brands fa-git-alt', 'order': 3},
            {'name': 'Data Cleaning', 'icon_class': 'fa-solid fa-broom', 'order': 4},
            {'name': 'Feature Engineering', 'icon_class': 'fa-solid fa-cogs', 'order': 5},
            {'name': 'Business Insights', 'icon_class': 'fa-solid fa-chart-bar', 'order': 6},
            {'name': 'TensorFlow / PyTorch', 'icon_class': 'fa-solid fa-brain', 'order': 7},
            {'name': 'Communication', 'icon_class': 'fa-solid fa-comments', 'order': 8},
            {'name': 'Problem Solving', 'icon_class': 'fa-solid fa-puzzle-piece', 'order': 9},
            {'name': 'Leadership', 'icon_class': 'fa-solid fa-users', 'order': 10},
        ]
        for sk in skills:
            Skill.objects.update_or_create(name=sk['name'], defaults=sk)
        self.stdout.write(self.style.SUCCESS(f'  [OK] {len(skills)} Skills'))

        self.stdout.write(self.style.SUCCESS('\nDatabase seeded successfully!'))
