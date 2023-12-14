```python
import unittest
from editor.editor import VideoEditor

class TestVideoEditor(unittest.TestCase):

    def setUp(self):
        self.editor = VideoEditor()

    def test_cut(self):
        # Assuming cut function returns True if successful
        self.assertTrue(self.editor.cut(0, 10))

    def test_trim(self):
        # Assuming trim function returns True if successful
        self.assertTrue(self.editor.trim(0, 10))

    def test_crop(self):
        # Assuming crop function returns True if successful
        self.assertTrue(self.editor.crop((100, 100, 200, 200)))

    def test_rotate(self):
        # Assuming rotate function returns True if successful
        self.assertTrue(self.editor.rotate(90))

    def test_add_text(self):
        # Assuming add_text function returns True if successful
        self.assertTrue(self.editor.add_text("Sample Text", (50, 50)))

    def test_add_effect(self):
        # Assuming add_effect function returns True if successful
        self.assertTrue(self.editor.add_effect("black_and_white"))

    def test_adjust_brightness(self):
        # Assuming adjust_brightness function returns True if successful
        self.assertTrue(self.editor.adjust_brightness(1.2))

    def test_adjust_contrast(self):
        # Assuming adjust_contrast function returns True if successful
        self.assertTrue(self.editor.adjust_contrast(1.2))

if __name__ == '__main__':
    unittest.main()
```