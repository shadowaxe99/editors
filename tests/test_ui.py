```python
import unittest
from flask import Flask, template_rendered
from contextlib import contextmanager
from editor.ui import create_app

@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

class TestUI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        with captured_templates(self.app) as templates:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(templates), 1)
            template, context = templates[0]
            self.assertEqual(template.name, 'index.html')

    def test_editor_page(self):
        with captured_templates(self.app) as templates:
            response = self.client.get('/editor')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(templates), 1)
            template, context = templates[0]
            self.assertEqual(template.name, 'editor.html')

    def test_login_page(self):
        with captured_templates(self.app) as templates:
            response = self.client.get('/login')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(templates), 1)
            template, context = templates[0]
            self.assertEqual(template.name, 'login.html')

    def test_register_page(self):
        with captured_templates(self.app) as templates:
            response = self.client.get('/register')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(templates), 1)
            template, context = templates[0]
            self.assertEqual(template.name, 'register.html')

if __name__ == '__main__':
    unittest.main()
```