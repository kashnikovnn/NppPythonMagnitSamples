path = "e:\\ERRORS\\"
from datetime import datetime, date, time
date = datetime.today()
date = date.strftime("%Y%m%d_%H-%M-%S")
text = editor.getText();
import re
result = re.findall('Events:.*wsocode=.*',text)
console.write("Naydeno - %s \n" % int(len(result)))
		
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x in seen:
            continue
        seen.add(x)
        result.append(x)
    return result
result = unique(result)
console.write("Uniq NAydeno - %s \n" % int(len(result)))
if len(result) > 0:	
	for str in result:
		console.write("%s \n" % str)
	import os
	folderpath = path + date + '\\'
	if os.path.exists(folderpath)==False:
		os.makedirs(folderpath);
	jmxpackages = []
	for s in result:
		notepad.new();
		editor.addText(s);
		wsoname = re.findall('wsocode=.{6}',s)
		console.write("WSOs \n")
		wsoname = re.findall('\d\d\d.{3}',wsoname[0])
		console.write("WSONAMES \n")
		for str in wsoname:
			console.write("%s \n" % str)
		wsoname = wsoname[0]
		savepath = folderpath +  wsoname + '.json'
		jmxpackages.append(wsoname + ".OB46.v1")
		notepad.runPluginCommand('JSTool', 'JSFormat')
	
		notepad.saveAs(savepath);
		console.write("%s \n" % savepath)
	notepad.new();
	for s in jmxpackages:
		editor.addText(s + '\n');
		console.write("%s \n" % s)	
	notepad.saveAs(folderpath + '!JMXPackageNames.txt');
else:
	notepad.messageBox("Json's not found");
