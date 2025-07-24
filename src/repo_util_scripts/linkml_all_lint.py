import subprocess
from pathlib import Path

schema_dir = Path("./src/vega_scverse/schema")

for yaml_file in schema_dir.glob("*.yaml"):
    print(f"Linting {yaml_file}")
    result = subprocess.run(
        [
            "linkml-lint",
            "--config",
            str(Path("./lint_config.yaml")),
            "--ignore-warnings",
            str(yaml_file)
        ],
        capture_output=True,
        check=True,
        text=True,
    )
    if result.returncode == 0:
        print(f"Done linting {yaml_file}.")
        if result.stdout.strip():  # Show even if returncode is 0 but there are warnings
            print(result.stdout)
