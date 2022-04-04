from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class My_Views_Test(TestCase):
    def test_product_homeview(self):
        url = reverse("modelapp.views.HomeView")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
