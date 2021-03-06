#!/usr/bin/python

# This version uses an array to store segments.
# Arrays require padding to be filled in non-sequential order.

# Encoded Message and Key, description starts at page 180 of The Jefferson Key 
encmsg = "XQXFEETHAPKLJHXREHNJFTSYOL:EJWIWMPZKLRIELCP1FESZROPPOBOUQDXMLZKRGVK2EPRISZXNOXE3"
keyList = [33, 28, 71, 11, 56, 40, 85, 64, 97]
SEGMENT_LENGTH = 5
SEGMENT_PLACEHOLDER_PHRASE = "NOT_SET"

# Establish storage for extracted parts of the encrypted message.
segmentList = []

# Process message through key.
startpos = 0
for key in keyList:
	# Parse key numbers; left digit is row sequence, right digit is offset from last pos.
	rownum = key / 10
	pos = key % 10
	
	# Adjust start pos based on current key number.
	startpos += pos
	
	# Extract segment and advance startpos.
	segment = encmsg[startpos:startpos+SEGMENT_LENGTH]
	startpos += SEGMENT_LENGTH
	
	# If segmentList is smaller than current row num, pad it up.
	if len(segmentList) < rownum:
		for x in range(0,rownum-len(segmentList)):
			segmentList.append(SEGMENT_PLACEHOLDER_PHRASE)
			
	segmentList[rownum-1] = segment

# Output segment list. 
for seg in segmentList:
	print(seg)		

# read message written vertically into segment list
for x in range(0,SEGMENT_LENGTH):
	for y in range(0,len(segmentList)):
		print segmentList[y][x],
		
		
	


