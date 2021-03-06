import pytest
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader

#Import most_active_cookie
spec = spec_from_loader("most_active_cookie", SourceFileLoader("most_active_cookie", "most_active_cookie"))
most_active_cookie = module_from_spec(spec)
spec.loader.exec_module(most_active_cookie)

def test_main_no_args(capsys):
	with pytest.raises(SystemExit) as error:
		most_active_cookie.main([])
	assert error.value.code == 2
	out, err = capsys.readouterr()
	assert out == ''
	assert err == 'usage: pytest [-h] -d DATE filename\npytest: error: the following arguments are required: filename, -d\n'

def test_main_no_filename_arg(capsys):
	with pytest.raises(SystemExit) as error:
		most_active_cookie.main(['-d', '2018-12-09'])
	assert error.value.code == 2
	out, err = capsys.readouterr()
	assert out == ''
	assert err == 'usage: pytest [-h] -d DATE filename\npytest: error: the following arguments are required: filename\n'

def test_main_no_date_arg(capsys):
	with pytest.raises(SystemExit) as error:
		most_active_cookie.main(['test.csv'])
	assert error.value.code == 2
	out, err = capsys.readouterr()
	assert out == ''
	assert err == 'usage: pytest [-h] -d DATE filename\npytest: error: the following arguments are required: -d\n'

def test_main_no_date_flag(capsys):
	with pytest.raises(SystemExit) as error:
		most_active_cookie.main(['test.csv', '2018-12-09'])
	assert error.value.code == 2
	out, err = capsys.readouterr()
	assert out == ''
	assert err == 'usage: pytest [-h] -d DATE filename\npytest: error: the following arguments are required: -d\n'

def test_main_non_csv_file(capsys):
	with pytest.raises(SystemExit) as error:
		most_active_cookie.main(['test.jpg', '-d', '2018-12-09'])
	assert error.value.code == 1
	out, err = capsys.readouterr()
	print(out)
	assert out == ''
	assert err == 'Must use a csv file\n'

def test_main_empty_csv(capsys):
	with pytest.raises(SystemExit) as error:
		most_active_cookie.main(['empty.csv', '-d', '2018-12-09'])
	assert error.value.code == 3
	out, err = capsys.readouterr()
	assert out == ''
	assert err == ''

def test_main_no_active_cookies_on_date(capsys):
	with pytest.raises(SystemExit) as error:
		most_active_cookie.main(['empty.csv', '-d', '2018-12-06'])
	assert error.value.code == 3
	out, err = capsys.readouterr()
	assert out == ''
	assert err == ''

def test_main_single_most_active_cookie(capsys):
	most_active_cookie.main(['test.csv', '-d', '2018-12-09'])
	out, err = capsys.readouterr()
	assert out == 'AtY0laUfhglK3lC7\n'
	assert err == ''

def test_main_multiple_most_active_cookie(capsys):
	most_active_cookie.main(['test.csv', '-d', '2018-12-07'])
	out, err = capsys.readouterr()
	assert out == '4sMM2LxV07bPJzwf\nAtY0laUfhglK3lC7\n'
	assert err == ''
