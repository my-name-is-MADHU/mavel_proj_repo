import pytest

from CreateMavenProject.app.app_maven_file import generate_pom


def test_generate_pom_success():
    result = generate_pom("demo")
    assert "<project>demo</project>" in result

def test_generate_pom_empty_name():
    with pytest.raises(ValueError):
        generate_pom("")
