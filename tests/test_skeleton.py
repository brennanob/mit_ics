from exercises.ps1 import count_vowels


def test_count_vowels(capsys):
    s = "azcbobobegghakl"
    count_vowels(s)
    captured = capsys.readouterr()
    assert captured.out == "Number of vowels: 5\n"
