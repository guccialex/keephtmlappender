import os


#create a directory where the files will be saved
os.system("mkdir OUTPUTFOLDER")

currentfolder = os.getcwd()

outputfolder = currentfolder + "/OUTPUTFOLDER"

inputfolder = currentfolder + "/Keep"



#copy the header file into the newfolder as the output file
os.system("cp NOTEHEADER.html ./OUTPUTFOLDER")


#open a new text and html file in the outputfolder directory

outputtext = open(outputfolder+"/APPENEDTEXT.txt", "w+")

outputhtml = open(outputfolder+"/NOTEHEADER.html", "a+")




#get each file inside the input folder

filesininput = os.listdir("Keep")


numberoffiles = len(filesininput)



fileslookedat = 0



#for each of the files in the input directory


while (fileslookedat < numberoffiles):

	currentfile = filesininput [fileslookedat]

	fileslookedat += 1

	#if the file is an html
	if (currentfile[-4:] == "html"):

		properfilename = inputfolder + "/" + currentfile

		#open the file 
		filecurrentfile = open(properfilename, "r")

		#put the contents into this variable
		currentfilecontents = filecurrentfile.read()

		#close the current file
		filecurrentfile.close()


		#get the stuff after the first <body>
		notebetweenbodybrackets = currentfilecontents.split("<body>", 1) [1]

		#get the stuff before the first </body>
		notebetweenbodybrackets = notebetweenbodybrackets.split("</body>", 1) [0]

		#print(notebetweenbodybrackets)


		#append to the output html
		outputhtml.write(notebetweenbodybrackets)


		#remove all the tags from the stuff in the body tag
		#except for the <br> tags which i need to convert to line breaks
		#basically convert all the tags I can and remove the others
		#then append to the outputtext.txt



#after all the appending, end it with a body tag and close everything
outputhtml.write("</body>")

outputhtml.close()

outputtext.close()