from docling.document_converter import DocumentConverter
from pathlib import Path
import pandas as pd

input_path = "C:\\Users\\Nitheesh kumar\\PycharmProjects\\docling document\\cities.pdf.md"
output_path = Path("csv_convert")

doc_conversion = DocumentConverter()
conversion =  doc_conversion.convert(input_path)
output_path.mkdir(parents=True, exist_ok=True)
doc_filename = conversion.input.file.stem
for i, table in enumerate(conversion.document.tables):
    table_convert: pd.DataFrame = table.export_to_dataframe()
    element_csv_file = output_path / f"{doc_filename}-table-{i + 1}.csv"
    table_convert.to_csv(element_csv_file)
    print(element_csv_file)
