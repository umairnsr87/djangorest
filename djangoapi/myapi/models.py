from django.db import models


# Create your models here.
# creating the model here
class data_for_verification(models.Model):
    STATUS_CHOICES = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    fnlwgt = models.PositiveIntegerField()
    education_num = models.PositiveIntegerField()
    capital_gain = models.PositiveIntegerField()
    capital_loss = models.PositiveIntegerField()
    hours_per_week = models.PositiveIntegerField()
    workclass_Private = models.CharField(max_length=20, choices=STATUS_CHOICES)
    workclass_Self_emp_not_inc = models.CharField(max_length=20, choices=STATUS_CHOICES)
    workclass_Local_gov = models.CharField(max_length=20, choices=STATUS_CHOICES)
    workclass_question_mark = models.CharField(max_length=20, choices=STATUS_CHOICES)
    workclass_State_gov = models.CharField(max_length=20, choices=STATUS_CHOICES)
    marital_status_Married_civ_spouse = models.CharField(max_length=20, choices=STATUS_CHOICES)
    marital_status_Never_married = models.CharField(max_length=20, choices=STATUS_CHOICES)
    occupation_Prof_specialty = models.CharField(max_length=20, choices=STATUS_CHOICES)
    occupation_Craft_repair = models.CharField(max_length=20, choices=STATUS_CHOICES)
    occupation_Exec_managerial = models.CharField(max_length=20, choices=STATUS_CHOICES)
    occupation_Adm_clerical = models.CharField(max_length=20, choices=STATUS_CHOICES)
    occupation_Sales = models.CharField(max_length=20, choices=STATUS_CHOICES)
    occupation_Other_service = models.CharField(max_length=20, choices=STATUS_CHOICES)
    occupation_Machine_op_inspct = models.CharField(max_length=20, choices=STATUS_CHOICES)
    occupation_question_unk = models.CharField(max_length=20, choices=STATUS_CHOICES)
    occupation_Transport_moving = models.CharField(max_length=20, choices=STATUS_CHOICES)
    relationship_Husband = models.CharField(max_length=20, choices=STATUS_CHOICES)
    relationship_Not_in_family = models.CharField(max_length=20, choices=STATUS_CHOICES)
    relationship_Own_child = models.CharField(max_length=20, choices=STATUS_CHOICES)
    relationship_Unmarried = models.CharField(max_length=20, choices=STATUS_CHOICES)
    race_White = models.CharField(max_length=20, choices=STATUS_CHOICES)
    sex_Male = models.CharField(max_length=20, choices=STATUS_CHOICES)


    def __str__(self):
        return str(self.firstname) + "-------" + str(self.lastname)
