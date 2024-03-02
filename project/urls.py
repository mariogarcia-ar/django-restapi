from rest_framework import routers
from . import api 

router = routers.DefaultRouter()

# crud 
router.register("api/projects", api.ProjectViewSet, 'projects')

urlpatterns = router.urls