from django.db import models

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestamo'
        
        
        
#ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)