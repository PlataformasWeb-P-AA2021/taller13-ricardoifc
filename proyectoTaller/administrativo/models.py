from django.db import models

class Edificio(models.Model):
    nombre = models.CharField("Nombre de edificio", max_length=30)
    direccion = models.CharField("Direccion", max_length=30)
    ciudad = models.CharField("Ciudad", max_length=30)
    tipo_opciones = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
        )
    tipo = models.CharField(max_length=12, choices=tipo_opciones)
    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

    def obtener_costo_cuartos(self):
        valor = [t.costoDep for t in self.departamentos.all()]
        valor = sum(valor)
        return valor

    def obtener_cantidad_departamentos(self):
        valor = len(self.departamentos.all())
        return valor

class Departamento(models.Model):
    propietario = models.CharField("Nombre de propietario", max_length=30)
    costoDep = models.DecimalField("Costo de departamento", max_digits=100, decimal_places=2)
    numCuartos = models.IntegerField("Numero de cuartos")
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")
    # Un dep pertenece a un edificio
    def __str__(self):
        return "%s %s %s %s" % (self.propietario, self.costoDep, self.numCuartos, self.edificio)

