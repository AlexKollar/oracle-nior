# Oracle Nior

Navi reads your fortune in coffee grounds, noir detective style. One line in, one reading out.

A **chip** for Apex — a small Python program Navi runs.
The chip format is `navi-chip/1` (see `navi-chip.json`).

## Files

- `root.py` — the entry point Navi runs
- `oracle-nior.png` — the chip as a forged chip (the whole
  file set rides inside the image).

## Install it in Navi

1. Open Navi's **Chips** tab, then **Navi User Repo (NUR)**.
2. **Search NUR** — every public repo tagged `navi-chips` is listed.
3. **Install** this chip. Navi downloads every Python file at the
   repo root at the latest release — `root.py` (or the entry named
   in `navi-chip.json`) is the chip, the other files are its modules —
   and forges them into a chip in the chips folder.

## Publishing an update

Edit the code, bump `version` in `navi-chip.json`, push, and publish
a new release — the version tag is created with that publish (this export is `0.1.0`). A newer release is what offers everyone who
installed the chip an update. Keep the `navi-chips` topic on the
repo — that is how Navi finds it.
