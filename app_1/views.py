from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q

#Create your views here.
def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        #sum=Data.objects.filter(first_name__icontains=q)
        multiple_q=Q(Q(first_name__icontains=q)|(Q(last_name__icontains=q))|Q(Age__icontains=q)|Q(date__icontains=q))
        sum=Data.objects.filter(multiple_q)
    else:
        sum=Data.objects.all()
    context={
        'data':sum
    }

    return render(request,'index.html',locals())
    
    
def showresult(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')

        sum=Data.objects.filter(Q(date=fromdate)&Q(date=todate))
        return render(request,'index.html',locals())

    else:
        sum=Data.objects.all()
    return render(request,'index.html',locals())


    
# # autoescape
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#         'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
#   }
#   return HttpResponse(template.render(context, request))
                  

# #block
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('childtemplate.html')
#   return HttpResponse(template.render())


# # cycle tag
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
#     }
#   return HttpResponse(template.render(context, request))


## extends
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('childtemplate.html')
#   return HttpResponse(template.render())
                  

# # filter
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   return render(request, "template.html")


# #firstof
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'x': 'Volvo',
#     'y': 'Ford',
#     'z': 'BMW',
#     }
#   return HttpResponse(template.render(context, request))



# # for
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'laptop': {
#       'brand': 'Apple',
#       'model': '12.089',
#       'year': '2010',
#      }
#     }
#   return HttpResponse(template.render(context, request))   
                  


# # if
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'value': 1
#   }
#   return HttpResponse(template.render(context, request))


# # ifchanged
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'list': ['apple','banana','pineapple','orange','guava','apple','apple','apple','pineapple','pineapple']
#     }
#   return HttpResponse(template.render(context, request))   



# # include, lorem, now
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   return HttpResponse(template.render())
                  


# # regroup
# from django.http import HttpResponse
# from django.template import loader
# def testing(request):
# #   template = loader.get_template('template.html')
#   context = {
#     'lap': (
#       {
#         'brand': 'Apple',
#         'model': 'i3',
#         'year': '2010',
#       },
#       {
#         'brand': 'lenovo',
#         'model': 'i3',
#         'year': '2011',
#       },
#       {
#         'brand': 'hp',
#         'model': 'i5',
#         'year': '2012',
#       },
#       {
#         'brand': 'hp',
#         'model': 'i3',
#         'year': '2016',
#       },
#       {
#         'brand': 'Apple',
#         'model': 'i5',
#         'year': '2011',
#       })
#     }
# #   return HttpResponse(template.render(context, request)) 
#   return render(request, "template.html",context)
              



# # resetcycle, spaceless, verbatim
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'books': ['maths', 'english', 'vedic', 'scientific','mahabaratha']
#     }
  
#   return HttpResponse(template.render(context, request))                  



# # templatetag, with
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#     template = loader.get_template('template.html')
#     return HttpResponse(template.render())                  











#  # first_name wishing
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstname': 'Emil',
#   }
#   return HttpResponse(template.render(context, request))                  








# FILTER REFERENCE

# # Add
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template_filter.html')
#   context = {
#     'value': [70, 35, 52],   
#   }
#   return HttpResponse(template.render(context, request))                    


# # check, add end of it
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   context = {
#     'books': ['maths', 'english', 'vedic', 'scientific','mahabaratha'],
#     'marbles':['red','yellow','blue','constant']
#     }
  
#   return render(request,'template_filter.html',context)          



# # add slashes, alert, capsfirst, center, cut
# from django.http import HttpResponse
# from django.shortcuts import render

# def testing(request):
#   context = {
#     'name': "jai srikrishna's" "gopalan's",   
#   }
#   return render(request,'template_filter.html',context)          


# # default, default_if_none
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template_filter.html')
#   context = {
#     'colors': ['Red', 'Green', 'Blue', [], 'Yellow','','','',(), {}, set(), range(0),None,False]
#   }
#   return HttpResponse(template.render(context, request))




# # dictsort, divisible by
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template_filter.html')
#   context = {
#     'cars': [
#       {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
#       {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
#       {'brand': 'Volvo', 'model': 'P1800', 'year': 1962},
#       {'brand': 'Ford', 'model': 'Focus', 'year': 2004},
#     ]
#   }

#   context = {
#     'totalsum': 40,
#   }
#   return render(request,'template_filter.html',context)          



# # timeuntil
# from django.http import HttpResponse
# from django.template import loader
# import datetime

# def testing(request):
#   template = loader.get_template('template_filter.html')
#   context = {
#     'marslanding': datetime.datetime(2050, 5, 17),
#     'moonlanding': datetime.datetime(1969, 7, 20),   
   
#   }
#   return HttpResponse(template.render(context, request))                     




# date since
from django.http import HttpResponse
from django.shortcuts import render,redirect
import datetime

def testing(request):
  context = {
    'mybirthdate': datetime.datetime(2001, 11, 18),   
  }
  return render(request, "template_filter.html",context)



