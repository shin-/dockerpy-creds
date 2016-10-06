import random
import sys

import pytest
import six

from dockerpycreds import (
    Store, StoreError, DEFAULT_LINUX_STORE, DEFAULT_OSX_STORE
)


class TestStore(object):
    def teardown_method(self, method):
        for server in self.tmp_keys:
            self.store.erase(server)

    def setup_method(self, method):
        self.tmp_keys = []
        if sys.platform.startswith('linux'):
            self.store = Store(DEFAULT_LINUX_STORE)
        elif sys.platform.startswith('darwin'):
            self.store = Store(DEFAULT_OSX_STORE)

    def get_random_servername(self):
        res = 'pycreds_test_{0:x}'.format(random.getrandbits(32))
        self.tmp_keys.append(res)
        return res

    def test_store_and_get(self):
        key = self.get_random_servername()
        self.store.store(server=key, username='user', secret='pass')
        data = self.store.get(key)
        assert data == {
            'ServerURL': '',
            'Username': 'user',
            'Secret': 'pass'
        }

    def test_get_nonexistent(self):
        key = self.get_random_servername()
        with pytest.raises(StoreError):
            self.store.get(key)

    def test_store_and_erase(self):
        key = self.get_random_servername()
        self.store.store(server=key, username='user', secret='pass')
        self.store.erase(key)
        with pytest.raises(StoreError):
            self.store.get(key)

    def test_unicode_strings(self):
        key = self.get_random_servername()
        key = six.u(key)
        self.store.store(server=key, username='user', secret='pass')
        data = self.store.get(key)
        assert data
        self.store.erase(key)
