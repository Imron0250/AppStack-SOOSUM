from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def Index(request):
    return render(request, 'index.html')


def ListInfo(request):
    context = {
        'info': Info.objects.all().order_by('-id')
    }
    return render(request, 'info-list.html', context)


def AddInfo(request):
    if request.method == 'POST':
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        logo = request.FILES['logo']
        Info.objects.create(
            logo=logo,
            text_ru=text_ru,
            text_uz=text_uz
        )
        return redirect('infoadd')
    return render(request, 'info-add.html')


def EditInfo(request, pk):
    if request.method == 'POST':
        i = Info.objects.get(id=pk)
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        logo = request.FILES['logo']
        i.text_uz=text_uz
        i.text_ru=text_ru
        i.logo=logo
        i.save()
        return redirect('infolist')
    return render(request, 'info-edit.html')


def DeleteInfo(request, pk):
    Info.objects.get(id=pk).delete()
    return redirect('infolist')


def addSocial_media(request):
    if request.method == 'POST':
        img = request.FILES['img']
        link = request.POST.get('link')
        SocialMedia.objects.create(
            img=img,
            link=link
        )
        return redirect('add-social-media')
    return render(request, 'add-social-media.html')

def SocialMediaInfo(request):
    context = {
        'social_media': SocialMedia.objects.all().order_by('-id')
    }
    return render(request, 'social-media-info.html', context)

def DeleteSocial_media(request, pk):
    SocialMedia.objects.get(id=pk).delete()
    return redirect('social-media-info')


def EditSocialMEdia(request, pk):
    if request.method == 'POST':
        i = SocialMedia.objects.get(id=pk)
        link = request.POST.get('link')
        img = request.FILES['img']
        i.link=link
        i.img=img
        i.save()
        return redirect('social-media-info')
    return render(request, 'social-media-edit.html')

def addProduct(request):
    if request.method == 'POST':
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        price = request.POST.get('price')
        img = request.FILES['img']
        Product.objects.create(
            img=img,
            name_ru=name_ru,
            name_uz=name_uz,
            price=price
        )
        return redirect('addProduct')
    return render(request, 'add-product.html')


def ProductInfo(request):
    context = {
        'product': Product.objects.all().order_by('-id')
    }
    return render(request, 'product-info.html', context)

def DeleteProduct(request, pk):
    Product.objects.get(id=pk).delete()
    return redirect('ProductInfo')

def EditProduct(request, pk):
    if request.method == 'POST':
        i = Product.objects.get(id=pk)
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        price = request.POST.get('price')
        img = request.FILES['img']
        i.name_uz=name_uz
        i.name_ru=name_ru
        i.price=price
        i.img=img
        i.save()
        return redirect('ProductInfo')
    return render(request, 'product-edit.html')



def addAboutProduct(request):
    if request.method == 'POST':
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        img = request.FILES['img']
        AboutProduct.objects.create(
            text_uz=text_uz,
            text_ru=text_ru,
            img=img,
        )
        return redirect('addAboutProduct')
    return render(request, 'add-about-product .html')


def AboutProductInfo(request):
    context = {
        'product_about': AboutProduct.objects.all().order_by('-id')
    }
    return render(request, 'about-product-info.html', context)

def DeleteAboutProduct(request, pk):
    AboutProduct.objects.get(id=pk).delete()
    return redirect('AboutProductInfo')

def EditAboutProduct(request, pk):
    if request.method == 'POST':
        i = AboutProduct.objects.get(id=pk)
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        img = request.FILES['img']
        i.text_uz=text_uz
        i.text_ru=text_ru
        i.img=img
        i.save()
        return redirect('AboutProductInfo')
    return render(request, 'about-product-edit .html')


def addAboutCompany(request):
    if request.method == 'POST':
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        AboutCompany.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            text_uz=text_uz,
            text_ru=text_ru,
        )
        return redirect('AboutCompanyList')
    return render(request, 'add-about-company.html')

def AboutCompanyList(request):
    context = {
        'about_company': AboutCompany.objects.all().order_by('-id')
    }
    return render(request, 'about-company-list.html', context)

def AboutCompanyEdit(request, pk):
    if request.method == 'POST':
        i = AboutCompany.objects.get(id=pk)
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        title_uz = title_uz
        i.title_ru = title_ru
        i.text_uz = text_uz
        i.text_ru = text_ru
        i.save()
        return redirect('AboutCompanyList')
    return render(request, 'about-company-edit.html')

def DeleteAboutCompany(request,pk):
    AboutCompany.objects.get(id=pk).delete()
    return redirect('AboutCompanyList')

def AddWhoUse(request):
    if request.method == 'POST':
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')    
        WhoUse.objects.create(
            title_uz = title_uz,
            title_ru = title_ru,
        )
        return redirect('WhoUseList')
    return render(request, 'add-who-use.html')

def EditWhoUse(request,pk):
    if request.method == 'POST':
        i = WhoUse.objects.get(id=pk)
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        i.title_uz = title_uz
        i.title_ru = title_ru
        i.save()
        return redirect('WhoUseList')
    return render(request, 'who-use-edit .html')
    
def WhoUseList(request):
    context = {
        'who_use': WhoUse.objects.all().order_by('-id')
    }
    return render(request, 'who-use-list.html', context)

def WhoUseDelete(request,pk):
    WhoUse.objects.get(id=pk).delete()
    return redirect('WhoUseList')


def OrderList(request):
    context = {
        'order': Order.objects.all().order_by('-id')
    }
    return render(request, 'order-list.html', context)

def OrderEdit(request,pk):
    if request.method == 'POST':
        i = Order.objects.get(id=pk)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        i.name = name
        i.phone = phone
        i.save()
        return redirect('OrderList')
    return render(request, 'order-edit.html')

def DeleteOrder(request, pk):
    Order.objects.get(id=pk).delete()
    return redirect('OrderList')



def AddDiscount(request):
    if request.method == 'POST':
        img = request.FILES['img']
        Discount.objects.create(
            img = request.FILES['img']
        )
        return redirect('DiscountList')
    return render(request, 'add-discount.html')

def EditDiscount(request,pk):
    if request.method == 'POST':
        i = Discount.objects.get(id=pk)
        img = request.FILES['img']
        i.save()
        return redirect('DiscountList')
    return render(request, 'discount-edit.html')
    
def DiscountList(request):
    context = {
        'discount': Discount.objects.all().order_by('-id')
    }
    return render(request, 'discount-list.html', context)

def DiscountDelete(request,pk):
    Discount.objects.get(id=pk).delete()
    return redirect('DiscountList')


def AddHowToUse(request):
    if request.method == 'POST':
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        HowToUse.objects.create(
            title_uz = title_uz,
            title_ru = title_ru,
            text_uz = text_uz,
            text_ru = text_ru,
        )
        return redirect('HowToUseList')
    return render(request, 'how-to-use-add.html')

def HowToUseDelete(request,pk):
    HowToUse.objects.get(id=pk).delete()
    return redirect('HowToUseList')

def EditHowToUse(request,pk):
    if request.method == 'POST':
        i = HowToUse.objects.get(id=pk)
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        i.title_uz = title_uz
        i.title_ru = title_ru
        i.text_uz = text_uz
        i.text_ru = text_ru
        i.save()
        return redirect('HowToUseList')
    return render(request, 'edit-how-to-use.html')

def HowToUseList(request):
    context = {
        'how_to_use': HowToUse.objects.all().order_by('-id')
    }
    return render(request, 'how-to-use-list.html', context) 

def AddFact(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        Fact.objects.create(
            number = number,
            text_uz = text_uz,
            text_ru = text_ru,
        )
        return redirect('FactList')
    return render(request, 'add-fact.html')

def FactList(request):
    context = {
        'fact': Fact.objects.all().order_by('-id')
    }
    return render(request, 'fact-list.html', context)

def EditFact(request,pk):
    if request.method == 'POST':
        i = Fact.objects.get(id=pk)
        number = request.POST.get('number')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        i.number = number
        i.text_uz = text_uz
        i.text_ru = text_ru
        i.save()
        return redirect('FactList')
    return render(request, 'edit-fact.html')

def DeleteFact(request,pk):
    Fact.objects.get(id=pk).delete()
    return redirect('FactList')
