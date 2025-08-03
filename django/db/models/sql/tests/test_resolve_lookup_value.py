import unittest
from collections import namedtuple

from django.db.models.sql.query import Query


class ResolveLookupValueTests(unittest.TestCase):
    def setUp(self):
        # Use a dummy Query instance; model is irrelevant for this test.
        self.query = Query(model=None)

    def test_namedtuple_preserved(self):
        NT = namedtuple('NT', ['start', 'end'])
        nt = NT(1, 2)
        resolved = self.query.resolve_lookup_value(nt, can_reuse=False, allow_joins=False)
        self.assertIsInstance(resolved, NT)
        self.assertEqual(resolved, nt)

    def test_plain_tuple(self):
        t = (1, 2, 3)
        resolved = self.query.resolve_lookup_value(t, can_reuse=False, allow_joins=False)
        self.assertIsInstance(resolved, tuple)
        self.assertEqual(resolved, t)

    def test_list_type_preserved(self):
        class MyList(list):
            pass

        l = MyList([1, 2, 3])
        resolved = self.query.resolve_lookup_value(l, can_reuse=False, allow_joins=False)
        self.assertIsInstance(resolved, MyList)
        self.assertEqual(resolved, l)

    def test_plain_list(self):
        l2 = [1, 2, 3]
        resolved2 = self.query.resolve_lookup_value(l2, can_reuse=False, allow_joins=False)
        self.assertIsInstance(resolved2, list)
        self.assertEqual(resolved2, l2)
