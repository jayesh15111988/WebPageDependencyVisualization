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

URLsConnectionHolder = [["source","target","value"]];

for individualLine in content:
    connectedNodesCollection = individualLine.rstrip().split(" ");
    numberOfConnectedNodesForCurrentNode = len(connectedNodesCollection) - 1;
    sourceNodeValue = connectedNodesCollection[0];
    if(numberOfConnectedNodesForCurrentNode > 0):
        del connectedNodesCollection[0];
        for individualTargetNode in connectedNodesCollection:
            URLsConnectionHolder.append([sourceNodeValue,individualTargetNode,numberOfConnectedNodesForCurrentNode+1]);
            #print("Source Node ",sourceNodeValue," and target node is ",individualTargetNode," and total connections for source ", numberOfConnectedNodesForCurrentNode);
    else:
        #numberOfConnectedNodesForCurrentNode is always zero and then we are scaling it to
        #constant value of r = 1 which is radius of URL node which is also dangling in the space
        URLsConnectionHolder.append([sourceNodeValue,sourceNodeValue,numberOfConnectedNodesForCurrentNode+1]);
        #print("Source Node ",numberOfConnectedNodesForCurrentNode[0]," and target node is ",numberOfConnectedNodesForCurrentNode[0]," connection ",numberOfConnectedNodesForCurrentNode);
writeListToCSVFile(URLsConnectionHolder,outputFileName);


