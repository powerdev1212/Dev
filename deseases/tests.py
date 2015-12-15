from django.test import TestCase

class DeseaseTests(TestCase):
    """ Tests for desease module. """
    
    def test_deseaseitem_related_items(self):
        """ Tests related_items attribute for DeseaseItem """
        from .models import DeseaseItem
        print "Get test items 'Leiomyosarcoma' by its old_id attribute..."
        try:
            items = DeseaseItem.objects.filter(active=True).count()
            print "Items ({0}) got from database - continue ...".format(items)
            #for i in items:
            #    print i.related_items
        except Exception as e:
            raise e
