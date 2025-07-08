import xml.etree.ElementTree as ET


def fix_coverage_xml(path_in='coverage.xml', path_out='coverage_fixed.xml'):
    tree = ET.parse(path_in)
    root = tree.getroot()
    sources = root.find('sources')
    if sources is not None:
        for source in sources.findall('source'):
            source.text = 'gendiff'
    tree.write(path_out)


if __name__ == '__main__':
    fix_coverage_xml()
