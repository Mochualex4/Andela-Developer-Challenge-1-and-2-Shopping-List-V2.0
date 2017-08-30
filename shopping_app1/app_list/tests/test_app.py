import os
import app_list
import unittest
import tempfile

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app_list.app.config['DATABASE'] = tempfile.mkstemp()
        app_list.app.testing = True
        self.app = app_list.app.test_client()
        with app_list.app.app_context():
            app_list.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app_list.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()