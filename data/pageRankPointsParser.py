import csv;

inputFileName = "pagerank.input.1000.1";
outputFileName = "pagerankVisualizationOutput.csv";

def writeListToCSVFile(listToWrite,fileName):
    with open(fileName, 'w', newline='') as fp:
        CSVFileWriter = csv.writer(fp, delimiter=',')
        for individualURLConnection in listToWrite:
            CSVFileWriter.writerow(individualURLConnection);

with open(inputFileName) as f:
    content = f.readlines();

URLsConnectionHolder = [];

for individualLine in content:
    connectedNodesCollection = individualLine.rstrip().split(" ");
    numberOfConnectedNodesForCurrentNode = len(connectedNodesCollection) - 1;
    sourceNodeValue = connectedNodesCollection[0];
    if(numberOfConnectedNodesForCurrentNode > 0):
        del connectedNodesCollection[0];
        for individualTargetNode in connectedNodesCollection:
            URLsConnectionHolder.append([sourceNodeValue,individualTargetNode]);
            #print("Source Node ",sourceNodeValue," and target node is ",individualTargetNode," and total connections for source ", numberOfConnectedNodesForCurrentNode);
    else:
        #numberOfConnectedNodesForCurrentNode is always zero and then we are scaling it to
        #constant value of r = 1 which is radius of URL node which is also dangling in the space
        URLsConnectionHolder.append([sourceNodeValue,sourceNodeValue]);
        #print("Source Node ",numberOfConnectedNodesForCurrentNode[0]," and target node is ",numberOfConnectedNodesForCurrentNode[0]," connection ",numberOfConnectedNodesForCurrentNode);
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

#print(webPagesIncomingLinkCounter," Links Counter ");
#Now in each connection assign how many inward link each target has. This will help us determine size
#of node while plotting it
for individualLinkDetails in URLsConnectionHolder:
    targetNodeValue = individualLinkDetails[1];
    if targetNodeValue in webPagesIncomingLinkCounter:
        individualLinkDetails.append(webPagesIncomingLinkCounter[targetNodeValue]);
    else:
        individualLinkDetails.append(0);

URLsConnectionHolder.insert(0,["source","target","value"]);
writeListToCSVFile(URLsConnectionHolder,outputFileName);


