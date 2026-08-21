"""Minimal example for CertViewer."""

from certviewer import certviewer


def main():
 runner = certviewer({"name": "CertViewer", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()