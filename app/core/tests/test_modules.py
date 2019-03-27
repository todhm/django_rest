from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test@londonappdev.com',password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email,password)


class ModelTests(TestCase):


    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = "fidel@crunchprice.com"
        password = "fidel123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_normalize_user_with_email(self):
        email = "test@BLKJSDLFKjDSF.com"
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'tests')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test1234'
        )
        self.assertEqual(user.is_staff,True)
        self.assertEqual(user.is_superuser,True)


    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(), 
            name='Vegan'
        )
        self.assertEqual(str(tag),tag.name)


    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)


    def test_recipe_str(self):
        recipe = models.Recipe.objects.create(
            user=sample_user(), 
            title='Steak and mushroom source',
            time_minutes=5, 
            price=5.00
        )
        self.assertEqual(str(recipe),recipe.title)