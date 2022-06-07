from main import encrypt


def test_case_1_encrpt():

    assert encrypt(origin="hello", key=5) == "mjqqt"


def test_case_2_encrpt():

    assert (
        encrypt(origin="abcdefghijklmnopqrstuvwxyz", key=3)
        == "defghijklmnopqrstuvwxyzabc"
    )


def test_case_3_encrpt():

    assert encrypt(origin="HELLO WORLD".lower(), key=4) == "LIPPS ASVPH".lower()


def test_case_4_encrpt():

    assert encrypt(origin="HELLO WORLD".lower(), key=-10) == "XUBBE MEHBT".lower()


def test_case_5_encrpt():

    assert encrypt(origin="HELLO - WORLD!".lower(), key=-10) == "XUBBE - MEHBT!".lower()
