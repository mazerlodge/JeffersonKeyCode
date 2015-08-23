#!/usr/bin/python

# This version uses a dictionary to store segments.
# Dictionary does not require padding found in the array version.

# Encoded Message and Key, description starts at page 180 of The Jefferson Key 
# Note: In the book the numbers 1, 2, and 3 are replaced by greek letters delta, phi, and theta.
encmsg = "XQXFEETHAPKLJHXREHNJFTSYOL:EJWIWMPZKLRIELCP1FESZROPPOBOUQDXMLZKRGVK2EPRISZXNOXE3"
keyList = [33, 28, 71, 11, 56, 40, 85, 64, 97]
SEGMENT_LENGTH = 5
SEGMENT_PLACEHOLDER_PHRASE = "NOT_SET"

# Establish storage for extracted parts of the encrypted message.
segmentDict = {}  # empty dictionary

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
	
	# Add segment to dictionary with rownum as key.
	segmentDict[rownum] = segment

# Output segment list from dictionary.
for x in range(1,len(segmentDict)+1):
	print segmentDict[x]

# read message written vertically into segments when displayed in row num order.
for x in range(0,SEGMENT_LENGTH):
	for y in range(1,len(segmentDict)+1):
		print segmentDict[y][x],
		
