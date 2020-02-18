from unittest import TestCase
import artwork_db

class TestArtWork(TestCase):
    def test_add_artist(self):
        self.assertEqual(1, artwork_db.add_artist('obj_artist'))
        
    def test_add_artwork(self):
        self.assertEqual(1, artwork_db.add_artwork('obj_artwork'))

    def test_search_artwork_by_artist_name(self):
        self.assertEqual(1, artwork_db.search_artwork_by_artist_name('obj_artist_Id'))

    def test_display_avaliable_artwork_by_artist(self):
        self.assertEqual(1, artwork_db.display_avaliable_artwork_by_artist('obj_avaliable_artwork'))

    def test_update_avaliability(self):
        self.assertEqual(1, artwork_db.update_avaliability('obj_art_name'))

    def test_delete_artwork(self):
        self.assertEqual(1, artwork_db.delete_artwork('obj_art_delete'))

    