#!/usr/bin/env python
# -*- coding: utf-8

"""Modelos para ubicacion de Proyectos de Grado"""

from django.db import models

class Tutor(models.Model):
    """
    Tutores asociados al Proyecto de Grado de los estudiantes
    """
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    cedula = models.CharField("cédula", max_length=9, unique=True)
    fecha_nacimiento = models.DateField("fecha de nacimiento", blank=True, null=True)

    def __unicode__(self):
        return "%s, %s" % (self.apellido, self.nombre)

class Tesis(models.Model):
    """
    Proyecto de Grado del estudiante
    """
    tutor = models.ForeignKey(Tutor)
    titulo = models.CharField("título", max_length=32)
    autor = models.CharField(max_length=32)
    resumen = models.TextField()
    palabras_claves = models.CharField(max_length=64)
    enlace_repositorio = models.URLField()
    
    def __unicode__(self):
        return self.autor
