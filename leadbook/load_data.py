# exec(open('load_data.py').read())
import csv
from contacts.models import Company, Contact
from django.forms.models import model_to_dict
from django.core import serializers
from django.forms.models import model_to_dict
# Company.objects.all()
# 
# from itertools import chain

# def to_dict(instance):
#     data = {}

#     data["id"]=instance.id
#     data["name"]=instance.name
#     data["email"]=instance.email
#     company_id =instance.company


#     return data
# t[0].company
# to_dict(t[0])

# t= Contact.objects.all()


# obj=Contact.objects.get(id=1)

# Contact.objects.all().count()


# dict_obj = model_to_dict( obj )

# with open('company.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')

#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(row[0],row[1],row[2],row[3])
#             c=Company(id=row[0],name=row[1],country=row[2],revenue=row[3])
#             c.save()
#             line_count += 1

#             # save to model
#     print(f'Processed {line_count} lines.')
# Contact.objects.all().delete()
with open('contact.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    
    for row in csv_reader:

        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print("---")
            print(row[0],row[1],row[2],row[3])

            # to get company infor based on company id
            print("company_id: ", row[3])
            company=Company.objects.get(id=row[3])
            print(company)
            c=Contact(id=row[0],name=row[1],email=row[2],company=company)
            c.save()
            line_count += 1

            # save to model
    print(f'Processed {line_count} lines.')

