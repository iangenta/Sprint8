from django.db import models

class TipoCliente(models.Model):
    customer_type_id = models.AutoField(primary_key=True)
    type_name = models.TextField(unique=True)
    debit_card = models.TextField()
    credit_card = models.TextField()
    current_account = models.TextField()
    checkbook_amount = models.IntegerField()
    box_dollar = models.TextField(blank=True, null=True)
    box_peso = models.TextField(blank=True, null=True)
    withdraw_daily_max = models.IntegerField(blank=True, null=True)
    transfer_comission = models.IntegerField(blank=True, null=True)
    max_travel_reception = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.type_name
    class Meta:
        managed = False
        db_table = 'tipo_cliente'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=55)
    customer_surname = models.CharField(max_length=55)  # This field type is a guess.
    customer_dni = models.CharField(max_length=55,db_column='customer_DNI')  # Field name made lowercase.
    dob = models.CharField(max_length=55,blank=True, null=True)
    customer_type = models.ForeignKey(TipoCliente, models.DO_NOTHING, blank=True, null=True)
    customer_address_id = models.IntegerField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.customer_name +' ' +self.customer_surname
    class Meta:
        managed = False
        db_table = 'cliente'

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