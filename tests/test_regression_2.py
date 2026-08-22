import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_regression_2():
 """Regression guard for a extract edge case discovered earlier."""
 from certviewer.features.feature-extract-2 import run_extract
 result = run_extract("sample-2", timeout=5)
 assert result["ok"] is True
 assert "value" in result