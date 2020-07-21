from empyloeeapi.viewsets import productViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('product', productViewset )