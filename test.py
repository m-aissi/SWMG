import unittest
from main import translate

class TestTranslate(unittest.TestCase):
    def test_translate_alphaabet(self):
        self.assertEqual(translate('abcdefghijklmnopqrstuvwxyz'), '𒋻𒁀𐏓𒁓𒀼𐎣𒋝𒀂𒐕𒑟𒐞𒁇𐎠𒐖𒆸𒇬𒌒𒇲𒑣𒈦𒑚𐎏𒉼𒉽𒌨𒑣')

    def test_translate_hello(self):
        self.assertEqual(translate('hello'), '𒀂𒀼𒁇𒁇𒆸')

    def test_translate_world(self):
        self.assertEqual(translate('world'), '𒉼𒆸𒇲𒁇𒁓')

    def test_translate_hello_world(self):
        self.assertEqual(translate('hello world'), '𒀂𒀼𒁇𒁇𒆸 𒉼𒆸𒇲𒁇𒁓')

    def test_translate_Hello_World(self):
        self.assertEqual(translate('Hello World'), '𒀂𒀼𒁇𒁇𒆸 𒉼𒆸𒇲𒁇𒁓')

    def test_translate_sentence(self):
        self.assertEqual(translate('Maledictum vinculi aeterni Ludio loricam tollere iam non potest'), '𐎠𒋻𒁇𒀼𒁓𒐕𐏓𒈦𒑚𐎠 𐎏𒐕𒐖𐏓𒑚𒁇𒐕 𒋻𒀼𒈦𒀼𒇲𒐖𒐕 𒁇𒑚𒁓𒐕𒆸 𒁇𒆸𒇲𒐕𐏓𒋻𐎠 𒈦𒆸𒁇𒁇𒀼𒇲𒀼 𒐕𒋻𐎠 𒐖𒆸𒐖 𒇬𒆸𒈦𒀼𒑣𒈦')

    def test_translate_sentence2(self):
        self.assertEqual(translate('Maledicta ablatione Perimit item cum ludio ludius moritur'), '𐎠𒋻𒁇𒀼𒁓𒐕𐏓𒈦𒋻 𒋻𒁀𒁇𒋻𒈦𒐕𒆸𒐖𒀼 𒇬𒀼𒇲𒐕𐎠𒐕𒈦 𒐕𒈦𒀼𐎠 𐏓𒑚𐎠 𒁇𒑚𒁓𒐕𒆸 𒁇𒑚𒁓𒐕𒑚𒑣 𐎠𒆸𒇲𒐕𒈦𒑚𒇲')
    

if __name__ == '__main__':
    unittest.main()
