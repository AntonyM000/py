import logging

values=[10,5,6,0,9,"hello",8,2]
for value in values:
    try:
        print(10/int(value))
    except ZeroDivisionError as e:
        pass
    except ValueError as e:
        print ("Hello World")
        raise
    # finally:
        # print("123")
    else:
        print("No exceptionJeeoe")





    # except (ValueError,ZeroDivisionError) as e:
    #     # print(str(e))
    #     pass
    # except AttributeError as e:
    #     # print(str(e))

    #     print("Hello World ")
    #     continue
    # except Exception as e:
    #     logging.exception(e)
    #     # continue
    #     #  pass
    # # print("operation failed")
