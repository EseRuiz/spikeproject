from rest_framework import routers
from enterprise.viewsets import EnterpriseViewSet

router=routers.SimpleRouter()
router.register('empresa',EnterpriseViewSet)
urlpatterns = router.urls