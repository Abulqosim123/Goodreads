# from django.http import JsonResponse
# from django.views import View
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import BookReview
from api.serializers import BookReviewSerializers
from rest_framework import generics
from rest_framework import viewsets


class BookReviewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializers
    queryset = BookReview.objects.all().order_by('-created_at')
    lookup_field = 'id'

#
# class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookReviewSerializers
#     queryset = BookReview.objects.all()
#     lookup_field = 'id'
#
#     # def get(self, request, id):
#     #     book_review = BookReview.objects.get(id=id)
#     #     serializer = BookReviewSerializers(book_review)
#     #     return Response(data=serializer.data)
#     #
#     # def delete(self, request, id):
#     #     book_review = BookReview.objects.get(id=id)
#     #     book_review.delete()
#     #
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
#     #
#     # def put(self, request, id):
#     #     book_review = BookReview.objects.get(id=id)
#     #     serializer = BookReviewSerializers(instance=book_review, data=request.data)
#     #
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #
#     # def patch(self, request, id):
#     #     book_review = BookReview.objects.get(id=id)
#     #     serializer = BookReviewSerializers(instance=book_review, data=request.data, partial=True)
#     #
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # json_response = {
#     #     'id': book_review.id,
#     #     'stars_given': book_review.stars_given,
#     #     'comment': book_review.comment,  # Change this line
#     #     'book': {
#     #         'id': book_review.book.id,
#     #         'title': book_review.book.title,
#     #         'description': book_review.book.description,
#     #         'isb': book_review.book.isb,
#     #     },
#     #     'user': {
#     #         'id': book_review.user.id,
#     #         'first_name': book_review.user.first_name,
#     #         'last_name': book_review.user.last_name,
#     #         'username': book_review.user.username,
#     #     }
#     # }
#     # return JsonResponse(json_response)
#
#
# class BookReviewAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         book_reviews = BookReview.objects.all().order_by('-created_at')
#
#         paginator = PageNumberPagination()
#         page_obj = paginator.paginate_queryset(book_reviews, request)
#         serializers = BookReviewSerializers(book_reviews, many=True)
#         return paginator.get_paginated_response(serializers.data)
#
#     def post(self, request):
#         serializer = BookReviewSerializers(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
