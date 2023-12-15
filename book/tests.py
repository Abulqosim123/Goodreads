from django.test import TestCase
from django.urls import reverse
from book.models import Book
from users.models import CustomUser


# Create your tests here.
class BookTestCase(TestCase):
    def test_no_book(self):
        response = self.client.get(reverse('book:list'))

        self.assertContains(response, "No books found")

    def test_books_list(self):
        book1 = Book.objects.create(title='Book1', description='description1', isb='6252525')
        book2 = Book.objects.create(title='Book2', description='description2', isb='62525256')
        book3 = Book.objects.create(title='Book3', description='description3', isb='62525257')

        response = self.client.get(reverse('book:list') + "?page_size=2")

        for book in [book1, book2]:
            self.assertContains(response, book.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("book:list") + "?page=2&page_size=2")

        self.assertContains(response, book3.title)

    def test_detail_page(self):
        book = Book.objects.create(title='Book', description='description', isb='6252525')

        response = self.client.get(reverse('book:detail', kwargs={'id': book.id}))
        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

    def test_search_books(self):
        book1 = Book.objects.create(title='Sport', description='description1', isb='6252525')
        book2 = Book.objects.create(title='Guide', description='description2', isb='62525256')
        book3 = Book.objects.create(title='Shoe Dog', description='description3', isb='62525257')

        response = self.client.get(reverse('book:list') + '?q=sport')
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse('book:list') + '?q=guide')
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse('book:list') + '?q=shoe')
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book2.title)


class BookReviewTestCase(TestCase):
    def test_add_review(self):
        book = Book.objects.create(title='Book1', description='Description1', isb='6252525')
        user = CustomUser.objects.create_user(
            username='Admin2', first_name='Abulqosim',
            last_name='Rafiqov', email='rafiqovbulqosim@gmail.com',
            password='somepassword'
        )
        self.client.login(username='Admin2', password='somepassword')

        self.client.post(reverse('book:reviews', kwargs={'id': book.id}), data={
            'stars_given': 3,
            'comment': 'Nice book'

        })
        book_reviews = book.bookreview_set.all()
        self.assertEqual(book_reviews.count(), 1)
        self.assertEqual(book_reviews[0].stars_given, 3)
        self.assertEqual(book_reviews[0].comment, 'Nice book')
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)
