from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):

    def Test_view_bag(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/save_movies.html')
        self.assertTemplateUsed(response, 'bag/bag.html')

    def Test_view_id_movies(self):
        movie = Item.objects.Create(name='Test bag movie')
        response = self.client.get(f'/id_movies/{movie.id}')
        self.assertTemplateUsed(response, 'bag/Amovie.html')
        self.assertRedirects(response, '/')
        updated_movie = Item.objects.get(id=movie.id)
        self.assertFalse(update_item.done)





        
