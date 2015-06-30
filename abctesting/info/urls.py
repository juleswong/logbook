from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
	# ex: /polls/
	url(r'^$', views.LogBookView.as_view(), name='logbook'),
	# ex: /polls/5/
	url(r'^(?P<pk>[0-9]+)/$', views.ChainOfCustodyView.as_view(), name='chainofcustody'),
	url(r'^logform/$', views.LogCreate.as_view(), name='logform'),
	url(r'^logform/(?P<pk>[0-9]+)/$', views.LogUpdate.as_view(), name='logformedit'),
	url(r'^customerform/$', views.CustomerCreate.as_view(), name='customerform'),
	url(r'^customerform/(?P<pk>[0-9]+)/$', views.CustomerUpdate.as_view(), name='customeredit'),
	url(r'^customers/$', views.CurrentCustomerView.as_view(), name='customers'),
	url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerInfoView.as_view(), name='customerinfo'),
	url(r'^api/$', views.SampleLogList.as_view()),
	url(r'^api/(?P<pk>[0-9]+)$', views.SampleLogDetail.as_view()),
	# ex: /polls/5/results/
	#url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# ex: /polls/5/vote/
	#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

urlpatterns = format_suffix_patterns(urlpatterns)