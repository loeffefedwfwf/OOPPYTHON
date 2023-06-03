from logexample import Logging, DEBUG
#log = Logging("Test log data!")
#log.BasicConfig(DEBUG)
#log.Log(3)
log = Logging()
log.BasicConfig(DEBUG)
while(True):
    try:
        digit1 = int(input("Enter digit1: "))
        digit2 = int(input("Enter digit2: "))
        log.Message = f"{digit1};\t{digit2}"
        log.Log(1)
        print(digit1/digit2)
    except Exception as ex:
        log.Message = ex
        log.Log(3)
    finally:
        yes = input("Do you want try again? [Y/N]:")
        if(yes.lower() != "y"):
            log.Message = "App has finished!"
            log.Log(1)
            break