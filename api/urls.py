from api.views import BookReviewSet

from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()

router.register(r'review', BookReviewSet, basename='review')
urlpatterns = router.urls



# from api.views import BookReviewDetailAPIView, BookReviewAPIView
# from django.urls import path
# path('review/', BookReviewAPIView.as_view(), name='review-list'),
# path('review/<int:id>/', BookReviewDetailAPIView.as_view(), name='review-detail')
