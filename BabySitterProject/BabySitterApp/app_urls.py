from django.urls.conf import path

from .views import babysitters, contact, gallery, parents, singlepage, typo, index

urlpatterns = [
    path('', index, name='index'),
    path('babysitters/', babysitters, name='babysitters'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('parents/', parents, name='parents'),
    path('singlepage/', singlepage, name='singlepage'),
    path('typo/', typo, name='typo'),
]