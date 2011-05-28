#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    class Meta:
        verbose_name_plural = "Tutores"

    def __unicode__(self):
        return "%s, %s" % (self.apellido, self.nombre)

class Autor(models.Model):
    """
    Estudiante
    """
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    cedula = models.CharField(max_length=9, unique=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "%s, %s" % (self.apellido, self.nombre)

class PalabraClave(models.Model):
    """
    Descriptores o palabras claves asociadas al tema del Proyecto de Grado
    """
    etiqueta = models.CharField(max_length=32)
    descripcion = models.TextField("descripción", blank=True)

    class Meta:
        verbose_name_plural = "Palabras claves"

    def __unicode__(self):
        return self.etiqueta

class Materia(models.Model):
    """
    Materias asociadas al tema de Proyecto de Grado
    """
    titulo = models.CharField(max_length=32)
    descripcion = models.TextField("descripción", blank=True)

    def __unicode__(self):
        return self.titulo

class Biblioteca(models.Model):
    """
    Biblioteca donde se encuentra la publicación asociada al Proyecto de Grado
    """
    nombre = models.CharField(max_length=32)
    direccion = models.TextField("dirección", blank=True)

    def __unicode__(self):
        return self.nombre

class ProyectoDeGrado(models.Model):
    """
    Proyecto de Grado del estudiante
    """
    tutor = models.ManyToManyField(Tutor)
    titulo = models.CharField("título", max_length=32)
    autor = models.OneToOneField(Autor)
    cota = models.CharField(max_length=16)
    resumen = models.TextField()
    fecha_publicacion = models.DateField("fecha de publicación", blank=True,
                                         null=True)
    palabra_clave = models.ManyToManyField(PalabraClave)
    enlace_repositorio = models.URLField()
    nota = models.PositiveIntegerField(blank=True)
    observacion = models.TextField("observación", blank=True)
    materia = models.ManyToManyField(Materia, blank=True)
    biblioteca = models.ForeignKey(Biblioteca)
    
    class Meta:
        verbose_name_plural = "Proyectos de Grado"

    def __unicode__(self):
        return self.titulo
