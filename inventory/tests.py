from django.test import TestCase
from django.urls import reverse
from .models import Inventory, Supplier

class InventoryTests(TestCase):

    def setUp(self):
        """Create test data before each test."""
        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.inventory = Inventory.objects.create(
            name="Test Item",
            description="Test Description",
            note="Test Note",
            stock=10,
            availability=True,
            supplier=self.supplier
        )

    def test_inventory_list_view(self):
        """Test if the inventory list page loads correctly."""
        response = self.client.get(reverse('inventory-list'))
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_view(self):
        """Test if an inventory detail page loads correctly."""
        response = self.client.get(reverse('inventory-detail', args=[self.inventory.id]))
        self.assertEqual(response.status_code, 200)

    def test_api_inventory_list(self):
        """Test if the API endpoint returns a 200 status code."""
        response = self.client.get(reverse('inventory-list'))
        self.assertEqual(response.status_code, 200)
