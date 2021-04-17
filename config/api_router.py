from rest_framework.routers import SimpleRouter
from django.urls import path

from epicevents.events.api import views

router = SimpleRouter()

router.register('clients', views.ClientViewSet)
router.register('contracts', views.ContractViewSet)
router.register('events', views.EventViewSet)

app_name = 'api'
urlpatterns = router.urls

# urlpatterns += [
#     path(
#         route='clients/',
#         view=views.ClientListView.as_view(),
#         name='client-list'
#         ),
# ]
# # urlpatterns += [
#     path(
#         route='clients/<int:client_pk>/contracts/',
#         view=views.ContractNestedViewSet.as_view({'get': 'list', 'post': 'create'}),
#         name='contract-list'
#         ),
#     path(
#         route='clients/<int:client_pk>/contracts/<int:pk>/',
#         view=views.ContractNestedViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#         name='contract-detail'
#         ),
#     path(
#         route='clients/<int:client_pk>/contracts/<int:pk>/events/',
#         view=views.EventNestedViewSet.as_view({'get': 'list', 'post': 'create'}),
#         name='event-list'
#         ),
#     path(
#         route='clients/<int:client_pk>/contracts/<int:contract_pk>/events/<int:event_pk>/',
#         view=views.EventNestedViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#         name='event-detail'
#         ),
# ]
