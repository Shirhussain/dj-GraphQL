from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Quiz(models.Model):
    """Model definition for Quize."""

    title = models.CharField(max_length=255, default= _("new Quiz"))
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(_("Date"), auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Quize."""

        verbose_name = 'Quize'
        verbose_name_plural = 'Quizes'

    def __str__(self):
        """Unicode representation of Quize."""
        return self.title


class Question(models.Model):
    """Model definition for Question."""

    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    )

    TYPE = (
        (0, _('Multiple Choice')),
    )
    quiz = models.ForeignKey(
        Quiz, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_("Type of Question"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return self.title


class Answer(models.Model):

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

