import os
import time
import zipfile



XML_OPT_TEMPLATE="""<?xml version="1.0" encoding="UTF-8"?>
<launch4jConfig>
	<dontWrapJar>false</dontWrapJar>
	<headerType>%s</headerType>
	<jar>%s</jar>
	<outfile>%s</outfile>
	<errTitle></errTitle>
	<cmdLine></cmdLine>
	<chdir>.</chdir>
	<priority>normal</priority>
	<downloadUrl>http://java.com/download</downloadUrl>
	<supportUrl></supportUrl>
	<stayAlive>true</stayAlive>
	<restartOnCrash>false</restartOnCrash>
	<manifest></manifest>
	<icon></icon>
	<classPath>
		<mainClass>%s</mainClass>
	</classPath>
	<jre>
		<path>C:\\Program Files (x86)\\Java\\jre1.8.0_231\\</path>
		<bundledJre64Bit>true</bundledJre64Bit>
		<bundledJreAsFallback>false</bundledJreAsFallback>
		<minVersion></minVersion>
		<maxVersion></maxVersion>
		<jdkPreference>preferJre</jdkPreference>
		<runtimeBits>64/32</runtimeBits>
	</jre>
</launch4jConfig>"""



jar=input("File Path?\t")
type_=input("Exe Type?\t")
mc=None
jar_zip=zipfile.ZipFile(jar,"r")
for k in str(jar_zip.read("META-INF/MANIFEST.MF"))[2:-1].split("\\n"):
	if (k.startswith("Main-Class:")):
		mc=k.split(":")[1].strip().replace("\\r","")
st=time.time()
cp=os.path.abspath(f"./tmp/xml-{st}.xml")
op=os.path.abspath(f"./tmp/{st}.exe")
with open(f"./tmp/xml-{st}.xml","w") as f:
	f.write(XML_OPT_TEMPLATE%(type_,jar,op,mc))
os.chdir("\\".join(jar.split("\\")[:-1]))
os.system(f"\"C:\\Program Files (x86)\\Launch4j\\launch4jc.exe\" {cp}")
with open(op,"rb") as rf,open(jar.split("\\")[-1]+".exe","wb") as wf:
	while (True):
		dt=rf.read(4096)
		wf.write(dt)
		if (len(dt)<4096):
			break
