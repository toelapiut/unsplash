from django.test import TestCase
from .models import Editor,tags
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

class tagsTest(TestCase):

    def setUp(self):
        self.tag=tags(name='nature')

    # test for checking instance
    def test_tag_isinstance(self):
        self.assertTrue(isinstance(self.tag,tags))
    
    # test for saving
    def test_save_tag(self):
        self.tag.save_tag()
        tagger=tags.objects.all()
        self.assertTrue(len(tagger)>0)

    #test for deleting editors

    def test_delete_tag(self):
        self.tag.save_tag()
        self.tag.delete_tag()
        tagger=tags.objects.all()
        self.assertTrue(len(tagger)==0)