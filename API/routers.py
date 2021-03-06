from rest_framework import routers
from Individual.views import IndividualUserViewSet
from Organization.views import OrgUserViewSet
from ShelterProvider.views import ShelterUserViewSet,ShelterEditUserViewSet,search


router = routers.DefaultRouter()
router.register(r'individualusers', IndividualUserViewSet,basename="Individual")
router.register(r'orgusers', OrgUserViewSet,basename="Organization")
router.register(r'shelterusers', ShelterUserViewSet,basename="Shelter")
router.register(r'profileEdit', ShelterEditUserViewSet,basename="Profile")
router.register(r'search', search,basename="Search")

