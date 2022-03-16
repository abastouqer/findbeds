from rest_framework import routers
from Individual.views import IndividualUserViewSet
from Organization.views import OrgUserViewSet
router = routers.DefaultRouter()
router.register(r'individualusers', IndividualUserViewSet,basename="Individual")
router.register(r'orgusers', OrgUserViewSet,basename="Organization")
