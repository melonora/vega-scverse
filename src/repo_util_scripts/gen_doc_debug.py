import subprocess
from pathlib import Path
from linkml.generators.docgen import DocGenerator

schema_path = Path("C:/Users/w-mv/PycharmProjects/vega_spatialdata/vega-scverse/src/vega_scverse/schema/specification.yaml")

gen = DocGenerator(
        schema_path,
        directory="doc",
        dialect="python",
        use_slot_uris=False,
        use_class_uris=False,
        hierarchical_class_view=False,
        index_name="index",
        subfolder_type_separation=False,
        render_imports=False,
        truncate_descriptions=True,
    )
print(gen.serialize())
