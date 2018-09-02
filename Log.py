import Util
def log(content):
    string = "[Time: " + Util.getYMDHMS() + "]: " + str(content)
    print(string)
    file = open("log.out", "a")
    file.write(string + "\n")
    file.close()
    return string