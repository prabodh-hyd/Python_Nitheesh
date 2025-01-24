from docling.document_converter import DocumentConverter
from pathlib import Path

first_10_pages = "C:\\Users\\Nitheesh kumar\\PycharmProjects\\file_conversion_2\\cities.pdf.md"

converter = DocumentConverter()
result = converter.convert(first_10_pages)
output_dir = Path("md_conversion")
output_dir.mkdir(parents = True, exist_ok = True)
doc_filename = Path(first_10_pages).stem

#converting to file formats by .html
html_filename = output_dir / f"{doc_filename}.html"
result.document.save_as_html(html_filename)

#converting to file formats by .yaml
yaml_filename = output_dir / f"{doc_filename}.yaml"
result.document.save_as_yaml(yaml_filename)

#converting to file formats by .xml
xml_filename = output_dir / f"{doc_filename}.xml"
result.document.save_as_document_tokens(xml_filename)

#converting to file formats by .html, .yaml, .xml, .json
json_filename = output_dir / f"{doc_filename}.json"
result.document.save_as_json(json_filename)

print(result)
