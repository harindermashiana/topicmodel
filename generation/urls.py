from django.conf.urls import url

from .views import FileFieldView
from . import views

urlpatterns = [
    url(r'^form/$', FileFieldView.as_view(),name='home'),
    url(r'^moreorless', views.modelx,name='moreorless'),
    url(r'runmodel',views.runmodel,name='runmodel')
    # url(r'^upload/$', views.Upload,name='uploadhome'),
    #url(r'^moreorless',views.option,name='option')
]
