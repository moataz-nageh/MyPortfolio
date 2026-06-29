"""
Admin configuration for portfolio models.
"""

from django.contrib import admin
from .models import (
    SiteConfig, HeroRole, Project, ProjectTechStack, Certificate, Testimonial,
    SocialLink, Service, Education, Experience, Skill
)
from django.utils.html import format_html


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    """Admin for the singleton site configuration."""
    list_display = ('site_title',)

    def has_add_permission(self, request):
        """Only allow one SiteConfig instance."""
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroRole)
class HeroRoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order')
    list_editable = ('display_order',)
    search_fields = ('title',)
    ordering = ('display_order', 'id')


class ProjectTechStackInline(admin.TabularInline):
    model = ProjectTechStack
    fields = ('order', 'name', 'icon_class')
    extra = 1
    ordering = ('order', 'id')
    show_change_link = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title', 'description', 'tech_stack__name')
    inlines = (ProjectTechStackInline,)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px; width:auto; border-radius:6px;" />', obj.image.url)
        return '-'
    image_preview.short_description = 'Image'


@admin.register(ProjectTechStack)
class ProjectTechStackAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'icon_class', 'order')
    list_editable = ('order',)
    list_filter = ('project',)
    search_fields = ('project__title', 'name', 'icon_class')
    ordering = ('project', 'order', 'id')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'issuer')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'order')
    list_editable = ('order', 'rating')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'order')
    list_editable = ('order',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'university', 'logo_preview', 'order')
    list_editable = ('order',)
    search_fields = ('degree', 'university')

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height:40px; width:auto; border-radius:6px;" />', obj.logo.url)
        return '-'
    logo_preview.short_description = 'Logo'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'company')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
