"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. Deterministic and offline: no input, no randomness,
no network, no dependencies -- the same bytes every run.
"""

import os

# Final fortune line: classic "You will..." fortune opening, a balanced
# mirror structure, and a quiet twist -- the deploy turns around and
# deploys on the developer (the weekend on-call that follows a Friday
# release). True about a developer's day, fresh, and lands in one breath.
FORTUNE = "You will deploy on Friday, and the weekend will deploy on you."


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
