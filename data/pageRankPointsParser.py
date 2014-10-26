import csv;

inputFileName = "pagerank.input.1000.1";
outputFileName = "pagerankVisualizationOutput.csv";

#Writing output data of PageRank algorithm in the output file
def writeListToCSVFile(listToWrite,fileName):
    with open(fileName, 'w', newline='') as fp:
        CSVFileWriter = csv.writer(fp, delimiter=',')
        for individualURLConnectionDetails in listToWrite:
            CSVFileWriter.writerow(individualURLConnectionDetails);

#Reading from input file
with open(inputFileName) as f:
    content = f.readlines();

#This array contains link details. Source, Target and number of incoming links to given target
URLsConnectionHolder = [];

#Read content in input file line by line
for individualLine in content:
    connectedNodesCollection = individualLine.rstrip().split(" ");
    numberOfConnectedNodesForCurrentNode = len(connectedNodesCollection) - 1;
    sourceNodeValue = connectedNodesCollection[0];
    if(numberOfConnectedNodesForCurrentNode > 0):
        del connectedNodesCollection[0];
        for individualTargetNode in connectedNodesCollection:
            URLsConnectionHolder.append([sourceNodeValue,individualTargetNode]);
    else:
        #numberOfConnectedNodesForCurrentNode is always zero and then we are scaling it to
        URLsConnectionHolder.append([sourceNodeValue,sourceNodeValue]);

#This will be used to keep track of how many incoming links current node has
webPagesIncomingLinkCounter = {};

#For each node collect how many inward links it has and we will base radius based on that
for individualLinkDetails in URLsConnectionHolder:
    targetNodeDetails = individualLinkDetails[1];
    #Node has self link - Just ignore that node
    if(individualLinkDetails[0] != individualLinkDetails[1]):
        if targetNodeDetails in webPagesIncomingLinkCounter:
            webPagesIncomingLinkCounter[targetNodeDetails] += 1;
        else:
            webPagesIncomingLinkCounter[targetNodeDetails] = 1;

#Now in each connection assign how many inward link each target has. This will help us determine size
#Of node while plotting it

for individualLinkDetails in URLsConnectionHolder:
    targetNodeValue = individualLinkDetails[1];
    if targetNodeValue in webPagesIncomingLinkCounter:
        individualLinkDetails.append(webPagesIncomingLinkCounter[targetNodeValue]);
    else:
        individualLinkDetails.append(0);

#Now Insert labels at the beginning of csv file for easier recognition in D3 code
URLsConnectionHolder.insert(0,["source","target","value"]);
writeListToCSVFile(URLsConnectionHolder,outputFileName);


