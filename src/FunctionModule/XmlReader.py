import xml.etree.ElementTree as Et

class XmlReader():

    dom = None
    
    def __init__(self,domPath):

        self.dom = Et.parse(domPath)

    def getXmlContext(self):

        root = self.dom.getroot()
        components = root.getchildren()
        for component in components:
            eles = component.getchildren()
            for ele in eles:
                yield (ele.tag,ele.attrib)

pass

