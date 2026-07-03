from django.core.management.base import BaseCommand
from faker import Faker
from store.models import Collection, Product, Customer, Order, OrderItem
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Collections
        collections = []
        collection_titles = ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports', 'Toys', 'Beauty', 'Automotive']
        for title in collection_titles:
            collection = Collection.objects.create(title=title)
            collections.append(collection)

        # Products
        products = []
        for _ in range(50):
            product = Product.objects.create(
                title=fake.catch_phrase(),
                slug=fake.slug(),
                description=fake.paragraph(nb_sentences=3),
                unit_price=round(random.uniform(5, 500), 2),
                inventory=random.randint(0, 100),
                collection=random.choice(collections),
            )
            products.append(product)

        # Customers
        customers = []
        for _ in range(20):
            customer = Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.unique.numerify('###-###-####'),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=80),
                membership=random.choice(['B', 'S', 'G']),
            )
            customers.append(customer)

        # Orders and OrderItems
        for _ in range(30):
            order = Order.objects.create(
                customer=random.choice(customers),
                payment_status=random.choice(['P', 'C', 'F']),
            )
            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=random.randint(1, 10),
                    unit_price=product.unit_price,
                )

        self.stdout.write(self.style.SUCCESS('Done! Seeded collections, products, customers, orders and order items.'))
