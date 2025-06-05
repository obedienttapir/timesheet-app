# timesync-tui

This is a minimal implementation of a Textual/Rich terminal application that aggregates Jira worklogs and exports them to Deltek SFT.

## Usage

1. Copy `config.txt.sample` to `config.txt` and edit the values.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run `python main.py`.

Tests use a local fixture and stub HTTP requests so no internet connection is required.
