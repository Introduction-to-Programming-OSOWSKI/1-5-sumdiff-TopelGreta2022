#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 12
day = 30

def test_code():
    assert main.sumDiff(10, 5) == 10, "sumDiff(10, 5) == 10 failed"
    assert main.sumDiff(17, 2) == 4, "sumDiff(17, 2) == 4 failed"
    assert main.sumDiff(123, 99) == 198, "sumDiff(123, 99) == 198 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
