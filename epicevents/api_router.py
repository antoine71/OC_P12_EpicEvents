from rest_framework.routers import SimpleRouter

from events.api.views import ClientViewSet, ContractViewSet, EventViewSet

router = SimpleRouter()

router.register('clients', ClientViewSet)
router.register('contracts', ContractViewSet)
router.register('events', EventViewSet)

app_name = 'api'
urlpatterns = router.urls
