from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),

    # INFO
    path('info/', AddInfo, name='infoadd'),
    path('infolist/', ListInfo, name='infolist'),
    path('infoedit/<int:pk>/', EditInfo, name='infoedit'),
    path('infodelete/<int:pk>/', DeleteInfo, name='infodelete'),
    path('add-social-media/', addSocial_media, name='add-social-media'),
    path('social-media-info/', SocialMediaInfo, name='social-media-info'),
    path('social-media-edit/<int:pk>/', EditSocialMEdia, name='social-media-edit'),
    path('social-media-delete/<int:pk>/', DeleteSocial_media, name='social-media-delete'),
    path('addProduct/', addProduct, name='addProduct'),
    path('ProductInfo/', ProductInfo, name='ProductInfo'),
    path('DeleteSocial_media/<int:pk>/', DeleteProduct, name='DeleteProduct'),
    path('EditProduct/<int:pk>/', EditProduct, name='EditProduct'),
    path('addAboutProduct/', addAboutProduct, name='addAboutProduct'),
    path('AboutProductInfo/', AboutProductInfo, name='AboutProductInfo'),
    path('DeleteAboutProduct/<int:pk>/', DeleteAboutProduct, name='DeleteAboutProduct'),
    path('EditAboutProduct/<int:pk>/', EditAboutProduct, name='EditAboutProduct'),
    path('add-About-Company/', addAboutCompany, name='addAboutCompany'),
    path('About-Company-List/', AboutCompanyList, name='AboutCompanyList'),
    path('About-Company-Edit/<int:pk>/', AboutCompanyEdit, name='AboutCompanyEdit'),
    path('Delete-About-Company/<int:pk>/', DeleteAboutCompany, name='DeleteAboutCompany'),
    path('Add-Who-Use/', AddWhoUse, name='AddWhoUse'),
    path('Edit-Who-Use/<int:pk>/', EditWhoUse, name='EditWhoUse'),
    path('Who-Use-List/', WhoUseList, name='WhoUseList'),
    path('Who-Use-Delete/<int:pk>/', WhoUseDelete, name='WhoUseDelete'),
    path('Order-List', OrderList, name='OrderList'),
    path('Order-Edit<int:pk>/', OrderEdit, name='OrderEdit'),
    path('Delete-Order<int:pk>/', DeleteOrder, name='DeleteOrder'),
    path('AddDiscount/', AddDiscount, name='AddDiscount'),
    path('EditDiscount/<int:pk>/', EditDiscount, name='EditDiscount'),
    path('DiscountList/', DiscountList, name='DiscountList'),
    path('DiscountDelete/<int:pk>/', DiscountDelete, name='DiscountDelete'),
    path('AddHowToUse/', AddHowToUse, name='AddHowToUse'),
    path('HowToUseDelete/<int:pk>/', HowToUseDelete, name='HowToUseDelete'),
    path('EditHowToUse/<int:pk>/', EditHowToUse, name='EditHowToUse'),
    path('HowToUseList/', HowToUseList, name='HowToUseList'),
    path('AddFact/', AddFact, name='AddFact'),
    path('FactList/', FactList, name='FactList'),
    path('EditFact/<int:pk>/', EditFact, name='EditFact'),
    path('DeleteFact/<int:pk>/', DeleteFact, name='DeleteFact'),
    #SOCIAL MEDIA

    #
]
