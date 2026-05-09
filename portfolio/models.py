"""
Portfolio models for dynamic content management.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class SiteConfig(models.Model):
    """
    Singleton model for global site settings.
    Stores personalized data like name, titles, descriptions, and CV link.
    Only one instance is allowed.
    """
    site_title = models.CharField(
        max_length=200,
        default='Moataz Nageh Saber | AI Engineer Portfolio'
    )
    meta_description = models.TextField(
        default='Portfolio of Moataz Nageh Saber — AI Engineer, '
                'and Data Analyst.'
    )
    og_image = models.ImageField(upload_to='site/', blank=True, null=True)
    name = models.CharField(max_length=200, default='Moataz Nageh Saber')
    hero_description = models.TextField(
        default='Transforming data into intelligent solutions through Machine Learning, AI, and advanced analytics.'
    )
    about_me = models.TextField(
        blank=True,
        help_text='Paragraph text for the About section.'
    )
    cv_link = models.URLField(blank=True, help_text='Link to Google Drive containing your CV')
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'

    def save(self, *args, **kwargs):
        """Ensure only one SiteConfig instance exists."""
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Prevent deletion of the singleton."""
        pass

    def __str__(self):
        return 'Site Configuration'


class Project(models.Model):
    """Portfolio project entry."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Certificate(models.Model):
    """Professional certificate or credential."""
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    link = models.URLField(blank=True, help_text='Link to view the certificate (e.g. Google Drive)')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title} — {self.issuer}'


class Testimonial(models.Model):
    """Client or peer testimonial with star rating."""
    name = models.CharField(max_length=200)
    review = models.TextField()
    rating = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name} — {self.rating}★'


class SocialLink(models.Model):
    """Dynamic social/contact link."""
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('twitter', 'Twitter'),
        ('other', 'Other'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.CharField(max_length=500, help_text='Full URL, mailto:, tel:, or https://wa.me/...')
    icon_class = models.CharField(
        max_length=100,
        help_text='Font Awesome class, e.g. "fa-brands fa-linkedin"'
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.get_platform_display()} — {self.url}'


class Service(models.Model):
    """Service offering card."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(
        max_length=100,
        help_text='Font Awesome class, e.g. "fa-solid fa-brain"'
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Education(models.Model):
    """Education history."""
    degree = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200, blank=True)
    university = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='universities/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} at {self.university}"


class Experience(models.Model):
    """Work or volunteer experience."""
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(
        max_length=100,
        default='fa-solid fa-building',
        help_text='Font Awesome class for the company icon'
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} at {self.company}"


class Skill(models.Model):
    """Technical skills with icons."""
    name = models.CharField(max_length=100)
    icon_class = models.CharField(
        max_length=100,
        help_text='Font Awesome class, e.g. "fa-brands fa-python"'
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
