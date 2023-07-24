import logging
import base64
import sys
import datetime, json
from datetime import datetime, timedelta , time
from json import JSONEncoder
import json
from decimal import Decimal
from django.utils.dateparse import parse_date
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import Group
from django.template import Context, Template
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import get_language
from django.contrib.auth.models import User
from django.contrib import messages
from decimal import Decimal
from django.db.models import Sum
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render , redirect
from.models import Ajaxvalue



class Index(View):
    template_name = "index.html"
    def get(self , request):
        print("HOMEEEE")

        adt_data = []

        adt = Ajaxvalue.objects.all()

        for ht in adt:
            data = {
                "id" : ht.id,
                "name" : ht.name,
                "age" : ht.age,
                "dept" : ht.dept,
            }

            adt_data.append(data)

        context = {
            'adt' : adt_data,
            'all_adt' : json.dumps(list(adt_data))
        }

        return render(request , self.template_name , context)
    
    def post(self , request):

        print("INNNNSIDE POST")

        data = request.body

        if(data):

            print("DATA === ",data)

            user_data = json.loads(data)['userData']

            print("USer DATA = ",user_data['adt_id'])

            if (int(user_data['age']) > 18):
            
                # db_param = {
                #     "name" : user_data['name'],
                #     "age" : user_data['age'],
                #     "dept" : user_data['dept'],
                # }

                if (user_data['adt_id'] == "0"):
                    del user_data['adt_id']
                    user_data['created_time'] = datetime.now()
                    Ajaxvalue.objects.create(**user_data)
                else:
                    del user_data['adt_id']
                    user_data['updated_time'] = datetime.now()
                    Ajaxvalue.objects.filter(id = int(user_data['adt_id'])).update(**user_data)
                return JsonResponse({'success' : True, 'message' : "You are Eligible"})
            
            else:
                return JsonResponse({'success' : True , 'message' : "You are not Eligible"})

        # adt_id = request.POST.get('adt_id')

        # db_param = {
        #     "name" : request.POST.get('name'),
            # "age" : request.POST.get('age'),
        #     "dept" : request.POST.get('dept'),
        # }

        # db_param = request.POST.dict()

        # del db_param['csrfmiddlewaretoken']
        # del db_param['adt_id']

        # print("DB Param = ",db_param)        

        # if(adt_id == '0'):
        #     print("New")
        #     db_param['created_time'] = datetime.now()
        #     Ajaxvalue.objects.create(**db_param)
        #     return redirect('summa')
        # else:
        #     print("Update")
        #     db_param['updated_time'] = datetime.now()
        #     Ajaxvalue.objects.filter(id = int(adt_id)).update(**db_param)

        #     return redirect('summa')
        

# def create(request):
#     if request.method == 'POST':
#         name=request.POST["name"]
#         age=int(request.POST["age"])
#         dept=request.POST["dept"]

#         new_Ajaxvalue = Ajaxvalue(name=name, age=age, dept=dept)
#         new_Ajaxvalue.save()
#         success = 'Form submitted successfully for'+ name
#         return HttpResponse(success)