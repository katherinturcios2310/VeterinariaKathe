from django.db import models

# Create your models here.
class colores(models.Model):
    pk_colores = models.AutoField(primary_key=True, null=False, blank=False)
    color = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'colores'
        verbose_name_plural = 'coloress'
        ordering = ['color']

    def __str__(self):
        return "{0}".format(self.color)

class especies(models.Model):
    pk_especies = models.AutoField(primary_key=True, null=False, blank=False)
    especie = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = 'especies'
        verbose_name_plural = 'especiess'
        ordering = ['especie']

    def __str__(self):
        return "{0}".format(self.especie)

class razas(models.Model):
    pk_razas = models.AutoField(primary_key=True, null=False, blank=False)
    raza = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = 'razas'
        verbose_name_plural = 'razass'
        ordering = ['raza']

    def __str__(self):
        return "{0}".format(self.raza)

class animales(models.Model):
    pk_colores = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length= 50, null=False, blank=False)
    fk_especies = models.ForeignKey(especies, on_delete=models.CASCADE, null=False, blank=False)
    fk_razas = models.ForeignKey(razas, on_delete=models.CASCADE, null=False, blank=False)
    diagnostico = models.CharField(max_length=500, null=False, blank=False)
    medicamentos = models.IntegerField(null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    imagen = models.URLField(max_length=8000, blank=False, null=False, default='https://i.ibb.co/0JZN3GS/6034d7d1f3e0f54a99b2b2bd-Mujercitas-louisa-may-alcott-editorial-alma.jpg')

    class Meta:
        verbose_name = 'animales'
        verbose_name_plural = 'animaless'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)
