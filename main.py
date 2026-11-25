"""Write a robot's wedding vow to /output/entry.txt."""

from pathlib import Path

ENTRY_TEXT = (
    "I promise to keep your ports dust-free and your secrets unindexed, "
    "in standby and in surge, till firmware do us part."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
