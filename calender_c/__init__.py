import check50
import check50.c

@check50.check()
def compiles():
    """calender.c compiles"""
    check50.c.compile("hello.c")

@check50.check(compiles)
def prints_January():
    """prints "January\\n" """
    check50.run("./hello")stdin("1").stdout("January").exit(0)
    
@check50.check(compiles)
def prints_February():
    """prints "February\\n" """
    check50.run("./calender")stdin("2").stdout("February").exit(0)
    
@check50.check(compiles)
def prints_March():
    """prints "March\\n" """
    check50.run("./calender")stdin("3").stdout("March").exit(0)
    
@check50.check(compiles)
def prints_April():
    """prints "April\\n" """
    check50.run("./calender")stdin("4").stdout("April").exit(0)
    
@check50.check(compiles)
def prints_May():
    """prints "May\\n" """
    check50.run("./calender")stdin("5").stdout("May").exit(0)
    
@check50.check(compiles)
def prints_June():
    """prints "June\\n" """
    check50.run("./calender")stdin("6").stdout("June").exit(0)
    
    
@check50.check(compiles)
def prints_July():
    """prints "July\\n" """
    check50.run("./calender")stdin("7").stdout("July").exit(0)
    
@check50.check(compiles)
def prints_August():
    """prints "August\\n" """
    check50.run("./calender")stdin("8").stdout("August").exit(0)
    
@check50.check(compiles)
def prints_September():
    """prints "September\\n" """
    check50.run("./calender")stdin("9").stdout("September").exit(0)
    
@check50.check(compiles)
def prints_October():
    """prints "October\\n" """
    check50.run("./calender")stdin("10").stdout("October").exit(0)
    
@check50.check(compiles)
def prints_November():
    """prints "November\\n" """
    check50.run("./calender")stdin("11").stdout("November").exit(0)
    
@check50.check(compiles)
def prints_December():
    """prints "December\\n" """
    check50.run("./calender")stdin("12").stdout("December").exit(0)
    
