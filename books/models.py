from django.db import models
from django.utils.translation import gettext as _

class Books(models.Model):
    """Model definition for Books."""

    title = models.CharField(_("Title"), max_length=100)
    excerpt = models.TextField(_("Excerpt"))

    class Meta:
        """Meta definition for Books."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Books."""
        return self.title

