from asyncio.windows_events import NULL
import os
import json
import xmltodict

directoryName = os.path.dirname(os.path.abspath(__file__))
print('Absolute Dir: ', directoryName)

svgInputFile = "PCR"

filePath = directoryName + "/" + svgInputFile + ".svg"
print('Absolute File: ', filePath)
with open(filePath) as svg_file:
    data_dict = xmltodict.parse(svg_file.read())
    svg_file.close()
    #print(data_dict)
    
    #Get image size
    getHeight = data_dict.get("svg","Key not found").get("@height","Key not found")
    getWidth = data_dict.get("svg","Key not found").get("@width","Key not found")
    print("Heigth: " + getHeight)
    print("Width: " + getWidth)

    #Get color (and line thickness)
    getColorAndLineString = "{" + data_dict.get("svg","Key not found").get("g","Key not found").get("path","Key not found").get("@style","Key not found") + "}"
    getColorAndLineString = getColorAndLineString.replace(";", "', ").replace(":", ": ").replace("{","{'").replace("}","'}").replace(" "," '").replace(":","':").replace("'",'"')
    print(getColorAndLineString)
    getColorAndLineDict = json.loads(getColorAndLineString)
    getFillColor = getColorAndLineDict["fill"]
    print("Color: " + getFillColor)

    #Get raw coordinates of path(s)
    getRawCoord = data_dict.get("svg","Key not found").get("g","Key not found").get("path","Key not found").get("@d","Key not found")
    #print("RawCoord: " + getRawCoord)

#alternativeTest1 = "M 35.181889,206.75697 35.261226,201.75697 37.110308,194.99165 38.959392,188.22634 41.665211,185.77761 44.371031,183.32888 45.268143,184.22598 46.165256,185.1231 43.25997,189.05272 40.354682,192.98232 V 195.70298 198.42364 H 41.526255 42.697827 L 44.480627,194.0903 46.263426,189.75697 50.309054,184.17284 54.354682,178.5887 55.445474,178.50617 56.536267,178.42364 54.064093,182.0903 51.591919,185.75697 49.749068,189.42162 47.906219,193.08629 48.57348,193.75354 49.240742,194.42081 53.671979,187.42222 58.103219,180.42364 67.774335,165.75697 77.445451,151.0903 80.900071,147.85789 84.354681,144.62546 V 148.92138 153.21729 L 77.917591,159.65438 71.480495,166.09148 66.584256,177.4888 61.688016,188.88612 V 190.32154 191.75697 H 62.410434 63.132852 L 65.779152,189.29157 68.425454,186.82616 67.632503,184.75977 66.839554,182.69337 68.263785,181.81314 69.688017,180.93293 V 182.34494 183.75697 H 70.85959 72.031162 L 73.761391,179.57982 75.491619,175.40269 78.396961,171.91316 81.302311,168.42364 86.258111,159.0903 91.213921,149.75697 90.476761,145.01682 89.739611,140.27666 91.898891,137.19386 94.058171,134.11106 89.970341,130.29065 85.882511,126.47025 84.926751,123.44694 83.970991,120.42364 80.500621,115.8666 77.030251,111.30956 78.550921,110.80267 80.071591,110.29578 79.385781,107.67322 78.699971,105.05068 80.900391,105.89506 83.100821,106.73944 82.363551,109.06237 81.626281,111.3853 84.103971,114.44513 86.581671,117.50496 91.001281,115.30016 95.420891,113.09537 97.010471,114.4146 98.600041,115.73384 99.430201,114.90368 100.26036,114.07351 105.30752,113.47783 110.35468,112.88215 115.24072,112.65289 120.12675,112.42364 121.11804,111.43521 122.10932,110.44677 123.96559,111.98734 125.82186,113.5279 127.97276,111.37699 130.12367,109.22609 130.3023,106.80142 130.48092,104.37677 131.4965,102.73354 132.51206,101.09032 H 135.10004 137.68802 V 99.678286 98.266266 L 139.0861,99.130326 140.48418,99.994386 139.17138,101.57621 137.85859,103.15802 137.43996,109.79083 137.02135,116.42364 131.01899,119.75697 125.01663,123.0903 119.13718,127.43458 113.25771,131.77885 108.44894,133.2196 103.64018,134.66033 103.45234,142.83126 103.2645,151.00218 100.5382,153.20981 97.811911,155.41742 96.241551,161.65389 94.671191,167.89036 89.470111,174.157 84.269031,180.42364 84.645191,183.65414 85.021351,186.88465 86.354681,187.27634 87.688021,187.66802 92.354681,181.4161 97.021351,175.16418 104.35468,166.46058 111.68802,157.75697 118.08588,144.97661 124.48375,132.19626 131.24751,125.64328 138.01128,119.0903 138.6521,120.83098 139.29291,122.57166 143.54183,127.2096 147.79074,131.84754 151.55846,133.80225 155.32616,135.75697 H 163.15587 170.98556 L 172.96872,131.01059 174.9519,126.26421 174.56624,102.0106 174.18059,77.756978 172.44098,74.423645 170.70136,71.090312 166.92894,67.090312 163.1565,63.090312 161.08858,58.132293 159.02064,53.174274 157.31607,53.828381 155.6115,54.482486 152.98519,52.562081 150.35887,50.641675 151.4679,49.53266 152.57691,48.423645 H 161.79912 171.02135 V 45.532695 42.641745 L 171.83067,40.532695 172.63999,38.423645 H 175.05495 177.46992 L 179.57896,37.614327 181.68802,36.805008 181.70843,33.94766 181.72886,31.090312 182.96522,29.135491 184.20158,27.180671 185.59604,30.848408 186.99051,34.516147 186.77762,35.469896 186.56471,36.423645 187.60905,42.743364 188.65339,49.063084 189.83737,48.331341 191.02135,47.5996 V 49.5996 51.5996 L 189.68513,52.42543 188.34891,53.251261 189.18887,58.50412 190.02885,63.756978 H 187.85843 185.68802 V 66.857893 69.958808 L 188.77395,72.857893 191.85989,75.756978 H 194.10729 196.35469 L 196.33427,73.423645 196.31385,71.090312 195.07131,69.125502 193.82878,67.160693 195.31926,66.239532 196.80973,65.31837 200.59057,70.537674 204.37141,75.756978 H 205.48447 206.59754 L 210.1209,82.230547 213.64426,88.704117 215.69553,96.710983 217.74679,104.71785 222.47787,116.57074 227.20895,128.42364 230.02589,134.34878 232.84283,140.27394 232.74263,144.34878 232.64243,148.42364 231.71919,160.42364 230.79595,172.42364 229.50535,176.65566 228.21475,180.88768 217.89321,187.78462 207.57167,194.68156 204.50971,203.21926 201.44775,211.75697 H 158.90122 116.35468 V 211.0434 210.32981 L 118.50803,207.0434 120.66138,203.75697 H 119.1747 117.68802 V 204.83889 205.92081 L 114.9694,208.83889 112.2508,211.75697 H 73.676678 35.102553 Z M 116.35468,202.42364 V 201.0903 H 115.76671 115.17872 L 114.35468,202.42364 113.53064,203.75697 H 114.94266 116.35468 Z M 103.02135,190.53269 V 189.3084 L 103.79686,186.86602 104.57238,184.42364 102.46353,187.01181 100.35468,189.59998 V 190.67848 191.75697 H 101.68802 103.02135 Z M 203.4669,99.445466 206.1761,95.800619 205.41577,95.040283 204.65543,94.279946 200.17173,97.013478 195.68802,99.747006 191.68802,99.794396 187.68802,99.841786 190.35469,101.85812 193.02135,103.87446 196.88953,103.48239 200.7577,103.09032 Z M 101.35468,109.5406 103.02135,108.86808 104.68802,109.5406 106.35468,110.21311 H 103.02135 99.688021 Z M 74.347309,105.07838 73.51589,103.73312 74.324339,101.18592 75.13279,98.638716 72.410403,97.774663 69.688017,96.910611 V 94.875635 92.840659 L 72.354683,92.14331 75.02135,91.445961 V 90.268137 89.090311 H 79.609331 84.197301 L 85.021351,90.423645 85.845391,91.756978 H 87.445981 89.046561 L 90.791681,88.962589 92.536811,86.168199 90.335131,83.735369 88.133451,81.302538 90.577401,80.042449 93.021351,78.782358 100.68802,78.569086 108.35468,78.355813 V 80.123062 81.890311 L 106.8889,83.356094 105.42312,84.821877 106.31208,87.622761 107.20105,90.423645 H 110.17787 113.15468 L 114.75468,92.023645 116.35468,93.623645 116.51266,90.356978 116.67064,87.090311 116.44139,85.367841 116.21215,83.645371 119.28342,85.367841 122.35468,87.090311 122.87802,87.391423 123.40135,87.692535 121.6137,89.846522 119.82606,92.000507 120.13698,96.617264 120.4479,101.23402 117.58484,99.701756 114.72179,98.169498 102.98094,98.629906 91.240091,99.090316 87.245491,102.04538 83.250891,105.00044 81.800751,100.84057 80.350611,96.680698 77.603931,99.166406 74.85725,101.65212 75.481141,104.03789 76.105031,106.42364 H 75.641879 75.178729 Z M 94.354681,105.09031 93.530641,103.75698 99.942661,103.73878 106.35468,103.72057 109.3745,102.91142 112.39431,102.10227 111.56518,104.26296 110.73604,106.42364 H 102.95739 95.178731 Z M 66.688016,92.321038 65.688016,91.312534 V 88.601422 85.890311 L 67.14639,87.348685 68.604763,88.807058 68.14639,91.068301 67.688016,93.329542 Z M 138.93447,86.090311 138.84759,80.423645 138.29135,68.1777 137.73511,55.931756 135.89116,50.844367 134.0472,45.756979 133.04444,43.090312 132.04168,40.423645 136.91384,47.443796 141.786,54.463948 143.20038,62.110462 144.61474,69.756978 143.94492,74.756978 143.2751,79.756978 H 145.14823 147.02135 V 84.023645 88.290311 L 145.42135,86.690311 143.82135,85.090311 H 142.75468 141.68802 V 88.423645 91.756978 H 140.35468 139.02135 Z M 128.35468,88.502334 V 86.581023 L 129.60732,85.80685 130.85996,85.032677 130.65691,87.728161 130.45387,90.423645 H 129.40428 128.35468 Z M 67.013627,79.645867 67.005904,79.090311 65.672008,71.090312 64.338112,63.090312 65.316875,59.090312 66.295639,55.090312 67.099727,67.090312 67.903814,79.090311 67.462582,79.645867 67.02135,80.201422 Z M 76.279894,72.513761 77.835891,70.638904 75.707845,69.447992 73.579802,68.25708 74.366362,66.20734 75.152921,64.157601 83.067001,61.957289 90.981091,59.756978 H 93.145761 95.310441 L 94.419111,63.423645 93.527791,67.090312 89.568671,71.090312 85.609541,75.090311 84.458631,73.243297 83.307721,71.396284 79.015811,72.89245 74.723901,74.388617 Z M 110.19507,69.561664 106.36063,67.572333 104.02432,65.458006 101.68802,63.343678 V 61.724785 60.105892 L 106.68802,59.279442 111.68802,58.452993 115.94266,58.43832 120.19731,58.423645 121.02135,59.756978 121.84539,61.090312 H 119.76671 117.68802 V 63.133277 65.176242 L 120.42194,66.187588 123.15587,67.198932 118.59268,69.374962 114.0295,71.550993 Z M 156.69215,38.484477 157.02135,36.423645 153.68802,36.567979 150.35468,36.712311 144.35468,37.658936 138.35468,38.60556 143.91378,35.961289 149.47287,33.317017 150.89639,30.657132 152.31992,27.997247 157.93062,27.049326 163.54131,26.101406 160.94799,24.174443 158.35468,22.247482 153.68802,22.926719 149.02135,23.605955 144.35468,24.368136 139.68802,25.130318 142.8278,23.768236 145.96759,22.406155 149.7003,19.748234 153.433,17.090312 H 159.04091 164.64883 L 171.12551,21.287062 177.6022,25.483811 176.89975,26.620395 176.19731,27.756979 H 173.67495 171.1526 L 164.42031,29.200798 157.68802,30.644616 V 31.74094 32.837264 L 163.15164,34.630455 168.61528,36.423645 168.81831,37.756979 169.02135,39.090312 162.69215,39.817811 156.36294,40.545309 Z M 171.02135,13.756978 165.02135,10.544145 159.9337,10.483895 154.84604,10.423645 152.24936,11.813345 149.65268,13.203045 147.33702,11.85389 145.02135,10.504735 147.38118,10.46419 149.741,10.423645 155.38118,6.8421886 161.02135,3.2607319 163.84118,3.4790087 166.66102,3.6972853 172.75824,6.3108666 178.85548,8.9244484 181.60508,11.674046 184.35468,14.423645 V 15.756978 17.090312 L 180.68802,17.030063 177.02135,16.969812 Z"
#aletrnativeTest2 = "M 124.42815,188.24383 125.50097,174.51501 127.24479,173.83705 128.9886,173.15908 V 159.09128 145.02349 H 126.9547 124.92081 V 134.07426 123.12504 L 120.34453,121.89865 115.76826,120.67225 107.02708,120.64448 98.285896,120.61671 93.806736,115.82133 89.327586,111.02596 79.666566,109.59501 70.005546,108.16407 V 106.50903 104.854 L 76.470686,103.56097 82.935826,102.26794 92.611666,103.55149 102.28751,104.83503 122.56896,102.35057 142.8504,99.866107 144.14418,92.969657 145.43796,86.073215 150.42907,84.820526 155.42018,83.567837 158.47558,84.740302 161.53097,85.912767 V 93.056497 100.20023 L 167.12419,101.7644 172.71741,103.32857 202.71741,103.12702 232.71741,102.92546 V 105.43217 107.93888 L 228.14114,109.16528 223.56486,110.39167 219.06015,110.41944 214.55544,110.44722 212.45214,114.37727 210.34884,118.30732 206.78736,119.31092 203.22588,120.31453 188.25561,122.72115 173.28534,125.12777 174.61128,133.4197 175.93721,141.71162 174.53415,171.84213 173.1311,201.97264 H 148.24321 123.35533 Z"

unprocessedPath = getRawCoord

lessSpacesPath = unprocessedPath.replace("M ", "M").replace("L ", "L").replace("V ", "V").replace("H ", "H")
lessSpacesPath = lessSpacesPath.replace(" M", "M").replace(" L", "L").replace(" V", "V").replace(" H", "H").replace(" Z", "Z")
currentPrefix = "L"
pathString = lessSpacesPath
charIndex = 0
for char in pathString:
    if char == " ":
        pathString = pathString.replace(" ",currentPrefix, 1)
    elif char == "V" or char == "L" or char == "H":
        currentPrefix=char
    elif char == "M":
        currentPrefix="L"
    charIndex += 1
moreSpacePath = pathString.replace("M", " M").replace("L", " L").replace("V", " V").replace("H", " H").replace("Z", " Z")
pathArray = moreSpacePath.split(" ")
pathArray.pop(0)

doubleTupleArray = []
arrayOfArrays = []
coordIndex = 0
firstCoord = []
previousCoord = []
for coord in pathArray:
    prefix = coord[0]
    suffix = coord[1:len(coord)]
    if prefix == "M":
        firstCoord = suffix.split(",")
        previousCoord = suffix.split(",")
    elif prefix == "L":
        previousCoord = suffix.split(",")
    elif prefix == "V":
        previousCoord = [previousCoord[0], suffix]
    elif prefix == "H":  
        previousCoord = [suffix, previousCoord[1]]
    elif prefix == "Z":
        previousCoord = firstCoord
    doubleTupleArray.append([previousCoord[0], previousCoord[1]])
    if prefix == "Z":
        arrayOfArrays.append(doubleTupleArray)
        doubleTupleArray=[]
    #print(previousCoord)
    coordIndex += 1
#print(arrayOfArrays)
numberOfPaths = len(arrayOfArrays)
#print("Number of Paths: " + str(numberOfPaths))
#for path in pathsArray
currentPathCount = 0
#print("a of a: " + str(len(arrayOfArrays)))
for currentPath in arrayOfArrays:
    currentCoordCount = 0
    #print("c of p: " + str(len(currentPath)))
    previousX = ""
    previousY = ""
    for currentCoord in currentPath:
        currentX = str(float(currentCoord[0])/float(getWidth))
        currentY = str(float(currentCoord[1])/float(getHeight))

        if currentCoordCount == 0:
            #line
            currentCoord = "setTimeout(function(){" + '\n'
            currentCoord = currentCoord + "var canvasPath"+ str(currentPathCount) + "x" + str(currentCoordCount) + " = canvasObject.getContext('2d');" + '\n'
            currentCoord = currentCoord + "canvasPath" + str(currentPathCount) + "x" + str(currentCoordCount) + ".beginPath();" + '\n'
            currentCoord = currentCoord + "canvasPath" + str(currentPathCount) + "x" + str(currentCoordCount) + ".moveTo(htmlScreenWidth*" + currentX + ", htmlScreenHeight*" + currentY + ");" + '\n'
            currentCoord = currentCoord + "canvasPath" + str(currentPathCount) + "x" + str(currentCoordCount) + ".strokeStyle = 'red';" + '\n'
            currentCoord = currentCoord + "canvasPath" + str(currentPathCount) + "x" + str(currentCoordCount) + ".stroke();" + '\n'
            currentCoord = currentCoord + "}," + str(currentPathCount+currentCoordCount) + "*10);" + '\n'
            arrayOfArrays[currentPathCount][currentCoordCount] = currentCoord
            currentCoordCount = currentCoordCount + 1
            previousX = currentX
            previousY = currentY
            #fill

        else:
            #line
            currentCoord = "setTimeout(function(){" + '\n'
            currentCoord = currentCoord + "var canvasPath"+ str(currentPathCount) + "x" + str(currentCoordCount) + " = canvasObject.getContext('2d');" + '\n'
            currentCoord = currentCoord + "canvasPath" + str(currentPathCount) + "x" + str(currentCoordCount) + ".beginPath();" + '\n'
            currentCoord = currentCoord + "canvasPath" + str(currentPathCount) + "x" + str(currentCoordCount) + ".moveTo(htmlScreenWidth*" + previousX + ", htmlScreenHeight*" + previousY + ");" + '\n'
            currentCoord = currentCoord + "canvasPath" + str(currentPathCount) + "x" + str(currentCoordCount) + ".lineTo(htmlScreenWidth*" + currentX + ", htmlScreenHeight*" + currentY + ");" + '\n'
            currentCoord = currentCoord + "canvasPath" + str(currentPathCount) + "x" + str(currentCoordCount) + ".strokeStyle = 'red';" + '\n'
            currentCoord = currentCoord + "canvasPath" + str(currentPathCount) + "x" + str(currentCoordCount) + ".stroke();" + '\n'
            currentCoord = currentCoord + "}," + str(currentPathCount+currentCoordCount) + "*10);" + '\n'
            arrayOfArrays[currentPathCount][currentCoordCount] = currentCoord
            currentCoordCount = currentCoordCount + 1
            previousX = currentX
            previousY = currentY
            #fill

    currentPathCount = currentPathCount + 1 
canvasPrefixArray = []
canvasPrefixArray.append("<html>" + '\n')
canvasPrefixArray.append("<head>" + '\n')
canvasPrefixArray.append("<style>" + '\n')
canvasPrefixArray.append("body {" + '\n')
canvasPrefixArray.append("background-color: black;" + '\n')
canvasPrefixArray.append("}" + '\n')
canvasPrefixArray.append("div.titleClass {" + '\n')
canvasPrefixArray.append("text-align: center;" + '\n')
canvasPrefixArray.append("color: red;" + '\n')
canvasPrefixArray.append("font-family: Impact;" + '\n')
canvasPrefixArray.append("font-size: 2.5em;" + '\n')
canvasPrefixArray.append("}" + '\n')
#Div External Class
canvasPrefixArray.append("div.svgDivClassExt {" + '\n')
canvasPrefixArray.append("}" + '\n')
#Div Middle Class
canvasPrefixArray.append("div.svgDivClassMid {" + '\n')
canvasPrefixArray.append("display: grid;" + '\n')
canvasPrefixArray.append("grid-template-columns: 1fr;" + '\n')
canvasPrefixArray.append("grid-template-rows: 90vh;" + '\n')
canvasPrefixArray.append("align-items: center;" + '\n')
canvasPrefixArray.append("justify-items: center;" + '\n')
canvasPrefixArray.append("}" + '\n')
#Div Internal Class
canvasPrefixArray.append("div.svgDivClassInt {" + '\n')
canvasPrefixArray.append("display: grid;" + '\n')
canvasPrefixArray.append("margin-top: 0;" + '\n')
canvasPrefixArray.append("margin-right: auto;" + '\n')
canvasPrefixArray.append("margin-bottom: 0;" + '\n')
canvasPrefixArray.append("margin-left: auto;" + '\n')
canvasPrefixArray.append("}" + '\n')
canvasPrefixArray.append("</style>" + '\n')
canvasPrefixArray.append("</head>" + '\n')
canvasPrefixArray.append("<body>" + '\n')
canvasPrefixArray.append("<div class='titleClass'>" + '\n')
canvasPrefixArray.append("" + '\n')
canvasPrefixArray.append("</div>" + '\n')
canvasPrefixArray.append("<div class='svgDivClassExt'>" + '\n')
canvasPrefixArray.append("<div class='svgDivClassMid'>" + '\n')
canvasPrefixArray.append("<div class='svgDivClassInt'>" + '\n')
canvasPrefixArray.append("<canvas id='svgCanvas', width='" + "512" + "' height='" + "480" + "' style='border:1px solid red;'>" + '\n')
canvasPrefixArray.append("Use another browser dude!" + '\n')
canvasPrefixArray.append("</canvas>" + '\n')
canvasPrefixArray.append("<script>" + '\n')
canvasPrefixArray.append("htmlScreenWidth = 512;" + '\n')
canvasPrefixArray.append("htmlScreenHeight = 480;" + '\n')
canvasPrefixArray.append("var canvasObject = document.getElementById('svgCanvas');" + '\n')
canvasSuffixArray = []
canvasSuffixArray.append("</script>" + '\n')
canvasSuffixArray.append("</div>" + '\n')
canvasSuffixArray.append("</div>" + '\n')
canvasSuffixArray.append("</div>" + '\n')
canvasSuffixArray.append("</body>" + '\n')
canvasSuffixArray.append("</html>" + '\n')

htmlOutputFile = directoryName + "/" + svgInputFile + "_line" + ".html"

try:
    with open(htmlOutputFile, 'w') as outputFile:
        outputFile.write("")
except FileNotFoundError:
    print('File not found!')

outputFile = open(htmlOutputFile, "a")
outputFile.writelines(canvasPrefixArray)
for array in arrayOfArrays:
    outputFile.writelines(array)
outputFile.writelines(canvasSuffixArray)
outputFile.close()
print("Done!")