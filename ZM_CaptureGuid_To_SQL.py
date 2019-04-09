result = []
def testContents(contents, lineNumber, totalLines):
	console.write(contents)
	if contents.strip() != '':
		result.append(contents.strip())
	
editor.forEachLine(testContents)	
notepad.new()
editor.addText ('select distinct capture_guid \n from whs.event_queue_in \n where capture_guid in (')
for x in result:
	editor.addText ('hextoraw(\'%s\'), \n' % x)
editor.deleteRange(editor.getLength()-3, 3)
editor.addText (');')