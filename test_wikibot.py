from mylib.bot import search
from click.testing import CliRunner
from wikibot import search_cli


def test_search():
    assert "Microsoft" in search("Microsoft", sentences=2)


def test_wiki_bot():
    runner = CliRunner()
    result = runner.invoke(search_cli, ["--name", "Microsoft", "--sentences", "2"])
    assert result.exit_code == 0
    assert "Microsoft" in result.output
