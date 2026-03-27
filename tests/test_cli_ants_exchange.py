from click.testing import CliRunner

from jupyter_book.cli.main import main


def test_ants_exchange_message_mode():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "ants-exchange",
            "--message",
            "I welcome instant download clarity",
        ],
    )

    assert result.exit_code == 0
    assert "Selected: ANT-07 — Immutable Knowing" in result.output


def test_ants_exchange_requires_message_or_interactive():
    runner = CliRunner()
    result = runner.invoke(main, ["ants-exchange"])

    assert result.exit_code != 0
    assert result.exception is not None
    assert "Provide at least one --message, or use --interactive." in str(result.exception)
