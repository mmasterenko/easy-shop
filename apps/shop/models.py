from django.db import models

from project.utils.model_mixin import CreateUpdateMixin, CreatorMixin, ArchiveMixin


class Product(CreateUpdateMixin, CreatorMixin, ArchiveMixin, models.Model):
    title = models.CharField(max_length=256, blank=False)
    text = models.TextField(blank=True)


class Category(CreateUpdateMixin, CreatorMixin, ArchiveMixin, models.Model):
    title = models.CharField(max_length=128, blank=False)


class Tag(CreateUpdateMixin, CreatorMixin, ArchiveMixin, models.Model):
    title = models.CharField(max_length=64, blank=False)


class Producer(CreateUpdateMixin, CreatorMixin, ArchiveMixin, models.Model):
    title = models.CharField(max_length=128, blank=False)
