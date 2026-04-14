from persistence.api_client import ApiClient
from persistence.repository import Repository
from services.cleaner import Cleaner
from services.analyzer import Analyzer
from ui.cli import CLI


def main():
    client = ApiClient()
    repo = Repository()
    cleaner = Cleaner()
    analyzer = Analyzer()
    cli = CLI()

    raw = client.fetch()
    records = cleaner.clean(raw["features"])
    repo.save(records)

    result = analyzer.analyze(repo.get_all())
    cli.display(result)


if __name__ == "__main__":
    main()