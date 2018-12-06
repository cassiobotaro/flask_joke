from unittest.mock import patch

from flask_joke.cli import main


@patch('builtins.print')
def test_cli(mocked_print):
    main()
    mocked_print.assert_called_once()
    s = '<p>Wenn ist das Nunstück git und Slotermeyer? Ja! ... '\
        '<strong>Beiherhund</strong> '\
        'das Oder die Flipperwaldt gersput.</p>'
    mocked_print.assert_called_with(s)
