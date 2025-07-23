import subprocess
from pathlib import Path

schema_dir = Path("./src/vega_scverse/schema")

for yaml_file in schema_dir.glob("*.yaml"):
    print(f"validating {yaml_file}")
    subprocess.run(
        [
            "linkml-validate",
            "-s",
            str(yaml_file)
        ],
        capture_output=True,
        check=True
    )