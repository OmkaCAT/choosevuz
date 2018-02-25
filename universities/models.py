# -*- coding: utf-8 -*-

from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Предмет ЕГЭ"
        verbose_name_plural = "Предметы ЕГЭ"

    def __str__(self):
        return self.title

class Specialty(models.Model):
    code = models.CharField(max_length=9)
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.title


class University(models.Model):
    short_title = models.CharField(max_length=200)
    full_title = models.TextField()
    specialties = models.ManyToManyField(Specialty, through='SpecialtyScoreForUniversity')

    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"

    def __str__(self):
        return self.short_title


class SpecialtyScoreForUniversity(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()
    subjects = models.ManyToManyField(Subject)
