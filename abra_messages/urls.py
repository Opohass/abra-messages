from django.urls import path, include
from .views import AbraMessageViewSet, AbraMessageUnradViewSet

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('abra_messages', AbraMessageViewSet.as_view(), name="abra_messages_list_or_create"),
    path('abra_messages/<int:pk>/', AbraMessageViewSet.as_view(), name="abra_messages_get_or_update"),
    path('abra_messages/read', AbraMessageUnradViewSet.as_view(), name="abra_messages_read"),


]