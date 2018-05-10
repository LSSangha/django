from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^div_zero/$', views.DivZero.as_view(), name='div_zero'),
    url(r'^undefined_variable/$', views.UndefinedVariable.as_view(), name='undefined_variable'),
    url(r'^type_error/$', views.TypeError.as_view(), name='type_error'),
    url(r'^wrong_num_args/$', views.WrongNumArgs.as_view(), name='wrong_num_args'),
    url(r'^index_error/$', views.IndexError.as_view(), name='index_error'),

    # url(r'^login/$', views.Login.as_view(), name='login_func'),
]