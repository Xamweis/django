from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from myshop.models import articles, customers, orders
from datetime import date

# Create your views here.
@csrf_exempt
def order(request):
    if request.method == "GET":
        return render(request, 'order.html')
    
    else:
        try:
            a = request.POST.get("article")
            art = articles.objects.get(name=a)
            
            c = request.POST.get("name")
            cust = customers.objects.get(name=c)

            pri = art.price
            print(pri)

        except Exception as e:
            return render(request, 'fail.html', {"error": e.args[0]})

        else:
            orders.objects.create(article=art, customer=cust)
            data = {
                "article": art, 
                "name": cust,
                "price": pri
                }
            return render(request, 'ordered.html', data)