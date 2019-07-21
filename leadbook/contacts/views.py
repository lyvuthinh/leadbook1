from .models import Contact, Company
from django.http import JsonResponse
from django.forms.models import model_to_dict
import request
import urllib.parse

# function to filter contact by contact id
def contact_id_filter(request, contact_id):
    response={}
    data=[]
    try:
        try:
            instance=Contact.objects.get(id=contact_id)
            instance_json=model_to_dict(instance) 
            instance_json["company"]=model_to_dict(instance.company)
            data.append(instance_json)

            # api message when being succesfull
            status_code=200
            message="succesfull"
        except Contact.DoesNotExist:
            # api message when "no result"
            status_code=200
            message="No result"
    except Exception as e:
        # api message when the endpoint is failed
        status_code=500
        message="Internal Server Error"      
          
    response["status_code"]=status_code
    response["message"]="message"
    response["data"]=data
    return JsonResponse(response, json_dumps_params={'indent': 4})

# function to filter contact by attributes of company and contact
def contact_filter(request):
    response={}
    data=[]

    # get all potential request params
    company_id=request.GET.get('company_id')
    revenue=request.GET.get('revenue_gte')
    name=request.GET.get('name')
    if name!=None:
        name_clean=urllib.parse.unquote(name)
    
    # contact filter
    try:
        try:
            # get all contacts (no filter)
            if company_id==None and revenue==None and name==None:
                print("all")
                instances=Contact.objects.all()
            # filter contact by company id
            elif company_id!=None:
                print("company_id")
                instances=Contact.objects.filter(company__id=company_id)
            # filter contact by revenue
            elif revenue!=None:
                print("revenue")
                instances=Contact.objects.select_related("company").filter(company__revenue__gte=revenue)
            # filter contact by name
            elif name!=None:
                print("name")
                instances=Contact.objects.filter(name=name_clean)
 
            for instance in instances:
                instance_json=model_to_dict(instance) 
                instance_json["company"]=model_to_dict(instance.company)
                data.append(instance_json)

            # api message when being succesfull
            status_code=200
            message="succesfull"        
        except Contact.DoesNotExist:
            # api message when "no result"
            status_code=200
            message="No result"
    except Exception as e:
        # api message when the endpoint is failed
        status_code=500
        message="Internal Server Error" 

    response["status_code"]=status_code
    response["message"]=message
    response["data"]=data
    return JsonResponse(response, json_dumps_params={'indent': 4})
