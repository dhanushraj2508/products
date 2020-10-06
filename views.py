from django.shortcuts import render
from productdetails.models import product
from django.contrib import messages
from productdetails.forms import pdforms

def pddisply(request):
    results=product.objects.all()
    return render(request, "index.html",{"product":results})

def pdinsert(request):
    if request.method=="POST":
        if request.POST.get('productcompany') and request.POST.get('productname') and request.POST.get('productprice'):
             savepd=product()
             savepd.productcompany=request.POST.get('productcompany')
             savepd.productname=request.POST.get('productname')
             savepd.productprice=request.POST.get('productprice')
             savepd.save()
             messages.success(request,"The Product " +savepd.productname+ " Details are saved successfully..!")
             return render(request, "create.html")
    else:
            return render(request, "create.html")

def pdedit(request,id):
    getproductdetails=product.objects.get(id=id)
    return render(request, 'edit.html', {"product":getproductdetails})

def pdupdate(request,id):
    pdupdate=product.objects.get(id=id)
    form=pdforms(request.POST, instance=pdupdate)
    if form.is_valid():
        form.save()
        messages.success(request, "The Product Details is updated successfully..!")
        return render(request, "edit.html", {"product":pdupdate})

def pddel(request,id):
    delproduct=product.objects.get(id=id)
    delproduct.delete()
    results=product.objects.all()
    return render(request, "index.html",{"product":results})
