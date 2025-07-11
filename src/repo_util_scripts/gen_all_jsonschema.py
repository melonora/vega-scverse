import subprocess
from pathlib import Path

schema_dir = Path("./src/vega_scverse/schema")
output_dir = Path("./src/json_schema")

output_dir.mkdir(parents=True, exist_ok=True)

for yaml_file in schema_dir.glob("*.yaml"):
    output_file = output_dir / f"{yaml_file.stem}.py"
    print(f"Generating {output_file} from {yaml_file}")
    subprocess.run(
        [
            "gen-json-schema",
            "--no-mergeimports",
            str(yaml_file)
        ],
        stdout=open(output_file, "w"),
        check=True
    )