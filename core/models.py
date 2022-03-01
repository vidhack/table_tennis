from django.db import models
from django.utils.text import slugify

class BasicConfiguration(models.Model):
    # Inheriting all models from BasicConfiguration model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameBaseConfig(BasicConfiguration):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(NameBaseConfig, self).save(*args, **kwargs)
