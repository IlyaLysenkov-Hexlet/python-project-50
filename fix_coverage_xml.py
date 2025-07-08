import xml.etree.ElementTree as ET

file_path = "coverage.xml"

tree = ET.parse(file_path)
root = tree.getroot()

# Найди элемент <source> и замени его текст на "."
for source in root.findall(".//sources/source"):
    print(f"Было: {source.text}")
    source.text = "."
    print(f"Стало: {source.text}")

tree.write(file_path, encoding="utf-8", xml_declaration=True)
print("✅ coverage.xml обновлён.")
