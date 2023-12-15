from django.test import TestCase
from django.urls import reverse

from book.models import Book, BookReview
from users.models import CustomUser


class HomePageTestCase(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(title='Book1', description='Description', isb='555156')
        user = CustomUser.objects.create_user(
            username='Admin2', first_name='Abulqosim',
            last_name='Rafiqov', email='rafiqovbulqosim@gmail.com',
            password='somepassword'
        )
        user.set_password('somepassword')
        user.save()
        review1 = BookReview.objects.create(book=book, user=user, stars_given=3, comment='very good book')
        review2 = BookReview.objects.create(book=book, user=user, stars_given=4, comment='useful book')
        review3 = BookReview.objects.create(book=book, user=user, stars_given=5, comment='nice book')
        response = self.client.get(reverse("home_page") + "?page_size=2")

        self.assertContains(response, review3.comment)
        self.assertContains(response, review2.comment)
        self.assertNotContains(response, review1.comment)
