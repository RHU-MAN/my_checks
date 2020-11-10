import check50


@check50.check()
def exists():
    """calender.py exists"""
    check50.exists("calender.py")



@check50.check(exists)
def test01():
    """input of 1 displays January"""
    check50.run("calender.py").stdin("1").stdout("January\n").exit(0)


@check50.check(exists)
def test02():
    """input of 2 displays February"""
    check50.run("calender.py").stdin("2").stdout("February").exit(0)


@check50.check(exists)
def test03():
    """input of 3 displays March"""
    check50.run("calender.py").stdin("3").stdout("March").exit(0)


@check50.check(exists)
def test04():
    """input of 4 displays April"""
    check50.run("calender.py").stdin("4").stdout("April").exit(0)


@check50.check(exists)
def test05():
    """input of 5 displays May"""
    check50.run("calender.py").stdin("5").stdout("May").exit(0)


@check50.check(exists)
def test06():
    """input of 6 displays June"""
    check50.run("calender.py").stdin("6").stdout("June").exit(0)
    
@check50.check(exists)
def test07():
    """input of 7 displays July"""
    check50.run("calender.py").stdin("7").stdout("July").exit(0)
    
@check50.check(exists)
def test08():
    """input of 8 displays August"""
    check50.run("calender.py").stdin("8").stdout("August").exit(0)
    
    
@check50.check(exists)
def test09():
    """input of 9 displays September"""
    check50.run("calender.py").stdin("9").stdout("Sepetember").exit(0)  
    
    
@check50.check(exists)
def test10():
    """input of 10 displays October"""
    check50.run("calender.py").stdin("10").stdout("October").exit(0)
    
    
@check50.check(exists)
def test11():
    """input of 11 displays November"""
    check50.run("calender.py").stdin("11").stdout("November").exit(0)
    
    
@check50.check(exists)
def test12():
    """input of 12 displays December"""
    check50.run("calender.py").stdin("12").stdout("December").exit(0)    
    
    
  
