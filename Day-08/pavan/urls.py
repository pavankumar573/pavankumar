from django .urls import  path
from pavan import views
urlpatterns=[
	path('',views.home),
	path('pavanbro/',views.chk),
	path('haritha/',views.haritha),
	path('log/',views.login),
	path('ff/',views.ff),
]