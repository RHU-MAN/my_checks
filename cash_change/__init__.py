import check50
import check50.c


@check50.check()
def exists():
    """cash.c exists"""
    check50.exists("cash.c")


@check50.check(exists)
def compiles():
    """cash.c compiles"""
    check50.c.compile("cash.c", lcs50=True)


@check50.check(compiles)
def test025():
    """input of 0.25 yields output of 2"""
    check50.run("./cash").stdin("0.25").stdout(coins(2), "2\n").exit(0)


@check50.check(compiles)
def test8():
    """input of 8 yields output of 8"""
    check50.run("./cash").stdin("0.01").stdout(coins(1), "1\n").exit(0)


@check50.check(compiles)
def test045():
    """input of 0.45 yields output of 3"""
    check50.run("./cash").stdin("0.45").stdout(coins(3), "3\n").exit(0)


@check50.check(compiles)
def test530():
    """input of 5.30 yields output of 12"""
    check50.run("./cash").stdin("5.30").stdout(coins(12), "12\n").exit(0)



@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("./cash").stdin("-1").reject()


@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./cash").stdin("foo").reject()


@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("./cash").stdin("").reject()

def coins(num):
    # regex that matches `num` not surrounded by any other numbers (so coins(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"


