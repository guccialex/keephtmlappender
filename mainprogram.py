import os

#gets the directory of the current path this python file is in
cdirectory = os.path.dirname(os.path.realpath(__file__))

#turns that string of the current location to bytes of it
bytecdirectory = os.fsencode(cdirectory)


#if it doesnt exist, create the directory in the current directory that will store the created text and html files
if (not os.path.exists(cdirectory)):
	os.makedirs(cdirectory+"/htmlandtext")

#the name of the path the new folder that will hold the created html and text files
newfolder = cdirectory + "/htmlandtext/"

#open a new text and html file in the newfolder directory
createdtext = open(newfolder+"APPENEDTEXT.txt", "w")
createdhtml = open(newfolder+"APPENEDHTML.html", "w")


#remembers if this is the first loop and if we've put the header at the beginning of the html
isheaderentered = False


#goes over each html file in the current directory
for file in os.listdir(cdirectory):
    filename = os.fsdecode(file)
    #print(filename)


    #if the file in this directory ends with .html it's one of the keep files
    if (filename.endswith(".html")):

    	#open the current html file stored in filename that's being looped over to read its contents
	    fileopened = open(filename, "r",encoding = "ISO-8859-1")
	    #get the text in that file
	    text = fileopened.read()

	    #gets the two parts of the html text, one for everything before and one for everything after the first <body> tag
	    beforeandafterbody = text.split("<body>",1)
	    #stores everything after the first body tag in afterbody
	    afterbody = beforeandafterbody[1]


	    #if the header hasn't been put in yet, we put the header in now
	    if (isheaderentered == False):
    		createdhtml.write(beforeandafterbody[0])
    		createdhtml.write("<body>")
    		isheaderentered = True



	    #Creates two indexes of everything before the last body tag and everything after the last body tag that was stored in afterbody
	    midbodyandfooter = afterbody.split("</body>")
	    #Stores everything between the first <body> tag and the last </body> tag in midbody
	    midbody = midbodyandfooter[0]


	    #writes the midbody to the html file
	    createdhtml.write(midbody)
	    createdtext.write(midbody)
	    
	    #closes the current keep html file being read
	    fileopened.close()

#adds in the closing body tags to the html file
createdhtml.write("</body>")
createdhtml.write("</html>")

createdhtml.close()
createdtext.close()