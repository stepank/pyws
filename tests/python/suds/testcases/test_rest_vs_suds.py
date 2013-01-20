import json
import unittest2 as unittest

from base import BaseTestCaseMixin


class RestVsSudsTestCase(BaseTestCaseMixin, unittest.TestCase):

    def test_create_item(self):
        content = json.dumps({'name': 'item100'})
        self.assertEqual(self.rest_client.put('some/item', content), 100)
        self.assertEqual(self.service.create_item('item100'), 100)

    def test_get_item(self):
        self.assertEqual(self.rest_client.get('some/item/100'), 'item100')
        self.assertEqual(self.service.get_item(100), 'item100')

    def test_get_items(self):
        items = ['item%s' % i for i in xrange(10)]
        self.assertEqual(self.rest_client.get('some/item'), items)
        self.assertEqual(list(self.service.get_items().item), items)

    def test_update_item(self):
        content = json.dumps({'name': 'item200'})
        self.assertEqual(
            self.rest_client.post('some/item/100', content), 'item200')
        self.assertEqual(
            self.service.update_item(100, 'item200'), 'item200')

    def test_delete_item(self):
        self.assertEqual(self.rest_client.delete('some/item/100'), True)
        self.assertEqual(self.service.delete_item(100), True)
