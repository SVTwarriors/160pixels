#Files in Folder JSON and index.html generator"

import os
import json

## Generate full File List ##
pyPath = os.path.dirname(os.path.abspath(__file__))
print("Path: " + pyPath)
fullFileListArray = os.listdir(pyPath)
print("Array: " + str(fullFileListArray))
fullFileListDict = {}
fullFileListDict["files"] = fullFileListArray
print("JSON: " + str(fullFileListDict))

print("write fullFileList.json")
fullFileListJSON = open(pyPath + "\\" + "index_fullFileList.json", 'w')
json.dump(fullFileListDict, fullFileListJSON, indent = 1)
fullFileListJSON.close()

## Generate html File List ##
htmlFileListArray = []
i=0
for fileElement in fullFileListArray:
    if fileElement[-5:] == ".html":
        htmlFileListArray.append(fullFileListArray[i])
    i=i+1
print("Array: " + str(htmlFileListArray))
htmlFileListDict = {}
htmlFileListDict["files"] = htmlFileListArray
print("JSON: " + str(htmlFileListDict))

print("write htmlFileList.json")
htmlFileListJSON = open(pyPath + "\\" + "index_htmlFileList.json", 'w')
json.dump(htmlFileListDict, htmlFileListJSON, indent = 1)
htmlFileListJSON.close()

## Generate json File List ##
jsonFileListArray = []
i=0
for fileElement in fullFileListArray:
    if fileElement[-5:] == ".json":
        jsonFileListArray.append(fullFileListArray[i])
    i=i+1
print("Array: " + str(jsonFileListArray))
jsonFileListDict = {}
jsonFileListDict["files"] = jsonFileListArray
print("JSON: " + str(jsonFileListDict))

print("write jsonFileList.json")
jsonFileListJSON = open(pyPath + "\\" + "index_jsonFileList.json", 'w')
json.dump(jsonFileListDict, jsonFileListJSON, indent = 1)
jsonFileListJSON.close()

## Generate bmp File List ##
bmpFileListArray = []
i=0
for fileElement in fullFileListArray:
    if fileElement[-4:] == ".bmp":
        bmpFileListArray.append(fullFileListArray[i])
    i=i+1
print("Array: " + str(bmpFileListArray))
bmpFileListDict = {}
bmpFileListDict["files"] = bmpFileListArray
print("JSON: " + str(bmpFileListDict))

print("write jsonFileList.json")
bmpFileListJSON = open(pyPath + "\\" + "index_bmpFileList.json", 'w')
json.dump(bmpFileListDict, bmpFileListJSON, indent = 1)
bmpFileListJSON.close()

metadata = "<meta charset='UTF-8'>"
metadata += "<meta name='description' content='A python generated index file.'>"
metadata += "<meta name='keywords' content='python generated index'>"

containerStyles = ".fullCont{" + "display: grid;" + "grid-template-columns: auto auto;" + "gap: 10px;" + "padding: 10px;" + "}"
containerStyles += ".titleCont{" + "display: grid;"+ "grid-column: 1 / 3;" + "color: white;" + "font-size:320%;" + "text-align: center;" + "}"
containerStyles += ".leftCont{" + "display: grid;"+ "width: 320px;" + "}"
containerStyles += ".rightCont{" + "display: grid;"+ "width: max;" + "}"

## Generate index.html##
hrefFileListArray = []
i = 0
for fileElement in htmlFileListArray:
    hrefString = "<table width=320 height=160 background='" + htmlFileListArray[i][0:-5] + "Banner.bmp'" + "><tr style='text-align:center;'><td><p style='font-size:280%;'><a href='" + htmlFileListArray[i] + "'>" + htmlFileListArray[i] + "</a></p></td></tr></table><br>"
    hrefFileListArray.append(hrefString)
    i=i+1

hrefFileListString = "".join(str(fileElement) for fileElement in hrefFileListArray)

indexString = "<html>" + "<head>" + metadata + "<style>a{text-decoration:none; color: white;}" + containerStyles + "</style>" + "</head>" + "<br>" + "<body bgcolor='black'>" + "<div id='fullCont' class='fullCont'>" + "<div id='titleCont' class='titleCont'>Robert's Random Projects</div><br>"+ hrefFileListString + "<div id='rightCont' class='rightCont'>blah blah</div>" + "</div>" + "</body>" + "</html>"
generatedIndex = open(pyPath + "\\" + "index.html", 'w')
generatedIndex.write(indexString)
generatedIndex.close()