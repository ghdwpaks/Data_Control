


class PrintLog :
    def Write(cont , filepath="resulttemp.txt") :
        f = open(filepath,'w',encoding="UTF-8")
        if type(cont) == type("") or type(cont) == type(0) :
            f.write(cont)
        elif type(cont) == type([]):
            for i in cont :
                f.write(str(i)+str("\n"))
        f.close()