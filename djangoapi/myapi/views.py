from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import data_for_verification
from .serializers import data_for_verification_serializer
import pickle
import json
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.externals import joblib
#import .form import MyForm


# Create your views here.
#creating class based view here
class approvalview(viewsets.ModelViewSet):
    #getting all the queryset
    queryset =data_for_verification.objects.all()
    #getting the serializer class
    serializer_class = data_for_verification_serializer



def myform(request):
    if(request.method=="POST"):
        form=MyForm(request.POST)
        if (form.is_valid()):
            myform=form.save(commit=False)
        else:
            form=MyForm()


@api_view(["POST"])
def approvereject(request):
    try:
        mdl=joblib.load(r"C:\Users\umairansari\Pictures\Downloads\census_income.pkl")
        mydata=request.data
        unit=np.array(list(mydata.values()))
        unit=unit.reshape(1,-1)
        scalars=joblib.load("")

    except:
        print("now values")

