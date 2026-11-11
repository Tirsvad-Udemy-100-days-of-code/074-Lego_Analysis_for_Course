import lego_analysis


def test_package_imports_with_version() -> None:
    assert lego_analysis.__version__ == "0.1.0"
