from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Print, Cart, CartPrint, UserProfile
#unittest
class PrintsTestCase(TestCase):

    # установка начальных значений для тестовых данных
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.print1 = Print.objects.create(title='Test Print 1', artist='Test Artist', description='Test Description', image='prints/testprint1.jpg', quantity=5, price=10.99)
        self.print2 = Print.objects.create(title='Test Print 2', artist='Test Artist', description='Test Description', image='prints/testprint2.jpg', quantity=3, price=19.99)
        self.cart = Cart.objects.create(user=self.user)
        self.cartprint1 = CartPrint.objects.create(cart=self.cart, print=self.print1, quantity=2)
        self.cartprint2 = CartPrint.objects.create(cart=self.cart, print=self.print2, quantity=1)
        self.profile = UserProfile.objects.create(user=self.user, address='123 Main St', city='Springfield', state='IL', country='US', zip_code='12345')

    # тест для страницы со списком печатей
    def test_prints_list_view(self):
        response = self.client.get(reverse('prints:prints-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prints/print-list.html')
        self.assertContains(response, self.print1.title)
        self.assertContains(response, self.print2.title)

    # тест для страницы корзины пользователя
    def test_cart_detail_view(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('cart:cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
        self.assertContains(response, self.print1.title)
        self.assertContains(response, self.print2.title)


