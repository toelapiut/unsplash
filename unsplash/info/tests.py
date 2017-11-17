from django.test import TestCase
from .models import Editor
# Create your tests here.
class EditorTest(TestCase):

    def setUp(self):
        self.editor=Editor(first_name='apiut',last_name='toel',email='toelapiut7@gmail.com',phone_number='071234567')

    # test for checking instance
    def test_isinstance(self):
        self.assertTrue(isinstance(self.editor,Editor))

    # test for saving
    def test_editor_save(self):
        self.editor.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)

    #test for deleting editors
    def test_editor_delete(self):
        self.editor.save_editor()
        self.editor.delete_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)==0)
