from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductModelSerializer
from rest_framework.renderers import JSONRenderer
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class InsertInput(View):
    @csrf_exempt
    def get(self,request):
        return render(request,'productinput.html')
class InsertView(View):
    @csrf_exempt
    def post(self,request):
        p_id=int(request.POST["t1"])
        p_name=request.POST["t2"]
        p_cost=float(request.POST["t3"])
        p_mfdt=request.POST["t4"]
        p_expdt=request.POST["t5"]
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        resp=HttpResponse("product inserted successfully")
        return resp
class DisplayView(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dic={"records":qs}
        return render(request,"display.html",con_dic)
class DeleteInputView(View):
    def get(self,request):
        return render(request,"deleteinput.html")
class DeleteView(View):
    def get(self,request):
        P_id=int(request.GET["t1"])
        prod=Product.objects.filter(pid=P_id)
        prod.delete()
        resp = HttpResponse("product deleted successfully")
        return resp
class UpdateInputView(View):
    def get(self,request):
        return render(request,"updateinput.html")
class UpdateView(View):
    def post(self,request):
        P_id=int(request.POST["t1"])
        p_name = request.POST["t2"]
        p_cost = float(request.POST["t3"])
        p_mfdt = request.POST["t4"]
        p_expdt = request.POST["t5"]
        prod=Product.objects.get(pid=P_id)
        prod.pname=p_name
        prod.pcost=p_cost
        prod.pmfdt=p_mfdt
        prod.pexpdt=p_expdt
        prod.save()
        resp = HttpResponse("product updated successfully")
        return resp

def productapi(request):
    products=Product.objects.all()
    ps=ProductModelSerializer(products,many=True)
    jsondata=JSONRenderer().render(ps.data)
    return HttpResponse(jsondata,content_type="application/json")







