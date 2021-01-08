from html.parser import HTMLParser

metacount = 0
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start tag found", tag)
        pos = self.getpos()
        print("At line ", pos[0], " and char ", pos[1])
        if len(attrs)>0:
            print("\nAttributes")
            for attr in attrs:
                print("\t",attr[0], " = ", attr[1])
        
        global metacount
        if tag=="meta":
            metacount+=1

    def handle_endtag(self, tag):
        print("Found end tag: ",tag)

    def handle_data(self, data):
        print("Found data: ",data)
    
    def handle_comment(self, comment):
        print("Handle comment: ",comment)


parser = MyHTMLParser()
file = open("google.html", "r")
if file.mode=="r":
    contents = file.read()
    parser.feed(contents)
    print(f"Meta tags {metacount} were found.")

