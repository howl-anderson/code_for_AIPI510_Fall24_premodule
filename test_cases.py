import filecmp
import pathlib

from acronym import main, get_acronym


def test_main(tmp_path: pathlib.Path, datadir: pathlib.Path):
    """
    test the main() function
    """

    input_file = datadir / "input_file_for_test.txt"
    actual_result_file = tmp_path / "result.txt"
    expected_result_file = datadir / "result_file_for_test.txt"

    main(input_file, actual_result_file)

    assert filecmp.cmp(actual_result_file, expected_result_file, shallow=False)


def test_get_acronym():
    """
    test the get_acronym() function
    """

    input_str = "United Nations"

    actual_result = get_acronym(input_str)

    assert actual_result == "UN"
