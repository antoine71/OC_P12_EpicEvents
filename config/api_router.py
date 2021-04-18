from rest_framework.routers import SimpleRouter

from epicevents.events.api import views

router = SimpleRouter()

router.register('clients', views.ClientViewSet)
router.register('contracts', views.ContractViewSet)
router.register('events', views.EventViewSet)

app_name = 'api'
urlpatterns = router.urls
