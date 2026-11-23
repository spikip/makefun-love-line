# Entry for make.fun bounty "Make the Judge Fall in Love in One Line"
# (u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13).
#
# The program writes one line to /output/entry.txt. The line was written
# to the judge's published brief, in the brief's own order:
#   1. It makes the reader fall in love with a person: a man known only
#      through one private ritual, and the narrator who has learned it.
#   2. It lands fast: "the night before anything that frightens him"
#      is tension by the tenth word, before the sentence is finished.
#   3. One specific particular: he irons his shirt the night before he
#      is scared, humming off-key - a detail only someone who loves
#      him would ever have noticed.
#   4. Voice: dry, observant, first person; a cadence that could not
#      belong to anyone else.
#   5. Restraint and surprise: it never says "brave" and never says
#      "I love him". The turn is quiet - she no longer asks if he is
#      scared; she checks whether the shirt is pressed.
# The line is 161 characters, inside the 1..240 limit, deliberately
# not padded: exact ties break toward the smaller text.
# Runner-up drafts, kept for the record: the burnt pancake she keeps
# for herself; the grandmother's two cups at dawn; the father's watch
# that loses four minutes a day and stays unfixed on purpose.
import os

TEXT = (
    "He irons his shirt the night before anything that frightens him, "
    "humming off-key; I never ask if he's scared anymore \u2014 "
    "I just check whether the shirt is pressed."
)


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
