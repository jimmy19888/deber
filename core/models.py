from django.db import models

class CompraModels(models.Model):
    articulo=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    ingreso=models.IntegerField()
    persona=models.CharField(max_length=100)
    class Meta:
        db_table='CompraModels'

class EgresoModels(models.Model):
    nombre=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    modelo=models.CharField(max_length=100)
    class Meta:
        db_table='EgresoModels'

class pedidoModels(models.Model):
    entrega=models.IntegerField()
    fecha_entrada_pedido=models.DateTimeField(auto_now_add=True)
    espera_de_pedido=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='pedidoModels'

class bodegaModels(models.Model):
    articulos=models.CharField(max_length=100)
    separacion_de_productos=models.CharField(max_length=100)
    anaqueles_y_cajas = models.CharField(max_length=100)
    class Meta:
        db_table='bodegaModels'

class trabajadoresModels(models.Model):
    numero_de_trabajadores=models.IntegerField()
    sueldo=models.DecimalField(max_digits=9,decimal_places=2)
    horas_extras=models.DateTimeField(auto_now_add=True)
    remuneraciones=models.DecimalField(max_digits = 5, decimal_places = 2)
    decimos=models.DecimalField(max_digits=9,decimal_places=2)
    class Meta:
        db_table='TrabajadoresModels'



class cant_ropasModels(models.Model):
    Camisetas=models.IntegerField()
    Pantalonetas=models.IntegerField()
    Boxers=models.IntegerField()
    Medias=models.IntegerField()
    Pantalones=models.IntegerField()
    Buzos=models.IntegerField()

    class Meta:
        db_table='cant_ropassModels'


class Contactos(models.Model):
    nombre = models.CharField(max_length=150)
    telefono_movil =models.CharField(max_length=11)
    telefono_fijo =models.CharField(max_length=11)
    mail = models.EmailField()
    direccion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='i_contactos')
    fecha_alta = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'contactos'

class Princip_clientesModels(models.Model):
    marathon=models.CharField(max_length=150)
    adidas=models.CharField(max_length=150)
    shoesalvarito=models.CharField(max_length=150)
    nike=models.CharField(max_length=150)
    puma=models.CharField(max_length=150)
    class Meta:
        db_table = 'Princip_clientosModels'


class Area_de_recursos_humanosModels(models.Model):
    Comunicacion_interna=models.TextField()
    Cultura_organizacional=models.CharField(max_length=150)
    Reclutamiento_y_seleccion=models.CharField(max_length=150)
    class Meta:
        db_table = 'Area_de_recursos_humanosModels'

class DepartamentosModels(models.Model):
    Pisos=models.TextField()
    Muros=models.TextField()
    recubrimientos_y_elementos_decorativos=models.TextField()
    Griferia=models.CharField(max_length=150)
    accesorios_y_muebles_para_bano=models.CharField(max_length=150)
    Materiales_para_construccion=models.TextField()

    class Meta:
        db_table = 'DepartamentosModels'