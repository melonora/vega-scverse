import subprocess
from pathlib import Path

schema_dir = Path("./src/vega_scverse/schema")

for yaml_file in schema_dir.glob("*.yaml"):
    print(f"Linting {yaml_file}")
    result = subprocess.run(
        [
            "linkml-lint",
            "--config",
            str(schema_dir.parent / "lint_config.yaml"),
            "--ignore-warnings",
            str(yaml_file)
        ],
        capture_output=True,
        check=True,
        text=True,
    )
    if result.returncode == 0:
        print(f"{yaml_file} passed linting.\n")
        if result.stdout.strip():  # Show even if returncode is 0 but there are warnings
            print(result.stdout)
    else:
        print(f"{yaml_file} has linting issues:\n")
        if result.stdout.strip():
            print(result.stdout)
        if result.stderr.strip():
            print(result.stderr)