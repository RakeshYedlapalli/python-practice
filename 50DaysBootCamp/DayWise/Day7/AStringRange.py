def stringRange():
    appendData = ''
    for x in range(0,6):
        print("")
        appendData += str(x) + "."
      #  print(x)
        #appendData = appendData.join(str(x))
        #appendData = appendData + ""

    print(appendData[:len(appendData)-1])


stringRange()
    
