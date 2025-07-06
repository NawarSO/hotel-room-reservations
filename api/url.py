from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users',       UserViewSet)
router.register(r'rooms',       RoomViewSet)
router.register(r'reservations',ReservationViewSet)
router.register(r'payments',    PaymentViewSet)
router.register(r'invoices',    InvoiceViewSet)
router.register(r'offers',      OfferViewSet)
router.register(r'complaints',  ComplaintViewSet)
router.register(r'responses',   ResponseViewSet)
router.register(r'reports',     ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),  # we remove 'api/' prefix here because we want the path api/rooms for example not api/api/rooms twice first by the main url and the second from here.
    
]