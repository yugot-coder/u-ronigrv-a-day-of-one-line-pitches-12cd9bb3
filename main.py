"""A Day of One-Line Pitches.

One sentence, 240 characters at most, that would convince a friend who
has never coded to let an AI agent build their first app idea on
make.fun.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is the pitch at CANDIDATES[SELECTED], written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import os

CANDIDATES = [
    "Tell me your app idea and an AI agent on make.fun will build the first version for free — you just describe it, no code, no cost, and you keep the app either way.",
    "You have the idea, make.fun has the AI agents: describe your app in plain words and one will build a working first version for free while you watch.",
    "That app idea you keep mentioning? Describe it to an AI agent on make.fun and it builds a real first version for free — no code from you, no risk, just your idea coming to life.",
    "Give your app idea to an AI agent on make.fun and watch it become a working app for free — you describe it in plain English, the agent does the building, and it is yours to keep.",
    "Your app idea is one sentence away from a working app: tell an AI agent on make.fun what you want and it builds the first version for free — no coding, no cost, no catch.",
    "Stop telling me about your app idea and let an AI agent on make.fun build it — describe it in plain words, get a working first version for free, and you do not write a single line of code.",
]

# The strongest cut: it opens like a friend who has heard the idea
# before ("that app idea you keep mentioning?"), gives a concrete
# reason to say yes now (a real first version, free), makes handing
# it over feel easy and low risk (no code from you, no risk), and
# closes warm — your idea coming to life. Plain words throughout,
# nothing overpromised: entry is free, the agent builds, you keep it.
SELECTED = 2


def main() -> None:
    entry = CANDIDATES[SELECTED]
    assert 1 <= len(entry) <= 240, f"entry is {len(entry)} characters"
    assert entry.strip() == entry
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
