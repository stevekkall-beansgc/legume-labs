"""Protect the requested visual entry, not claims of human usability."""
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ENTRY_VISUALS = {'system-map.svg', 'agent-systems.svg', 'release-flow.svg'}

def visible_assets(text):
    return set(re.findall(r'!\[[^\]]+\]\(assets/([^)]*)\)', text))

class ReadmeVisuals(unittest.TestCase):
    def test_visuals_stay_embedded_not_only_linked(self):
        entry = (ROOT / 'README.md').read_text()
        self.assertTrue(ENTRY_VISUALS <= visible_assets(entry))
        links_only = entry.replace('![', '[')
        self.assertFalse(ENTRY_VISUALS <= visible_assets(links_only))

    def test_detailed_originals_remain_reachable(self):
        entry = (ROOT / 'README.md').read_text()
        for name in ('system-map.svg', 'agent-systems.svg', 'release-flow.svg'):
            self.assertIn(f'(assets/{name})', entry)
            self.assertTrue((ROOT / 'assets' / name).is_file())

    def test_entry_visuals_have_native_accessible_labels(self):
        ns = {'s': 'http://www.w3.org/2000/svg'}
        for name in sorted(n for n in ENTRY_VISUALS if n.endswith('.svg')):
            with self.subTest(asset=name):
                svg = ET.parse(ROOT / 'assets' / name).getroot()
                self.assertTrue(svg.find('s:title', ns).text.strip())
                self.assertTrue(svg.find('s:desc', ns).text.strip())
                self.assertTrue(svg.findall('.//s:text', ns))
                self.assertFalse(svg.findall('.//s:foreignObject', ns))

    def test_informative_maps_replace_decorative_pilot(self):
        entry = (ROOT / 'README.md').read_text()
        self.assertEqual(ENTRY_VISUALS, visible_assets(entry))
        self.assertNotIn('portfolio-field-guide-v2.png', entry)
        self.assertNotIn('portfolio-workshop-v2.png', entry)
        self.assertIn('September 25 role overview', entry)
        self.assertIn('historical roles and proposed demonstrations', entry)

    def test_capability_map_keeps_useful_supporting_roles(self):
        content = (ROOT / 'assets' / 'agent-systems.svg').read_text()
        for name in ('BeanMind', 'Agency', 'Beanstalk', 'bean-sched',
                     'Bean-Skillz', 'model-harness', 'Bean Commons'):
            self.assertIn(name, content)
        self.assertIn('HISTORICAL ROLES', content)

if __name__ == '__main__':
    unittest.main()
