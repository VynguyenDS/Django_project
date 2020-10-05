from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import ProductDetails
import json
def mainpage(request):
    data = ProductDetails.objects.all()
    responseData = []
    for i in data:

        case = {'img': str(i.imgFile) }
        responseData.append(case)

    return render(request,'mainpage.html',{'responseData':responseData})
def table_page(request):
    return render(request,'table_page.html')
# this is function for admin inserts
def product_details(request):
    return render(request,'admin/product_details.html')
def insert_products(request):
    if request.method == 'POST':
        nameProduct = request.POST['idProducts']
        contentProduct = request.POST['content']
        imgFileProduct = request.POST['imgFile']
        case = {'nameProduct': nameProduct, 'contentProduct': contentProduct, 'imgFileProduct': imgFileProduct}
        data = ProductDetails(nameProduct = nameProduct,content = contentProduct, imgFile = imgFileProduct)
        data.save()
        responseData = []

        responseData.append(case)

        return HttpResponse(json.dumps(responseData), content_type="application/json")
