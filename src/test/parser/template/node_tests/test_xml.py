import xml.etree.ElementTree as ET

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.template.nodes.xml import TemplateXMLNode
from programy.parser.template.nodes.word import TemplateWordNode

from test.parser.template.base import TemplateTestsBaseClass


class TemplateXMLNodeTests(TemplateTestsBaseClass):

    def test_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)

        xml = TemplateXMLNode()
        xml._name = "dial"
        root.append(xml)

        xml.append(TemplateWordNode("07777777777"))

        self.assertEqual(len(root.children), 1)

        resolved = root.resolve(self.bot, self.clientid)
        self.assertIsNotNone(resolved)
        self.assertEqual("<dial>07777777777</dial>", resolved)

    def test_node_with_attribs(self):
        root = TemplateNode()
        self.assertIsNotNone(root)

        xml = TemplateXMLNode()
        xml._name = "dial"
        xml._attribs['leave_message'] = "true"
        root.append(xml)

        xml.append(TemplateWordNode("07777777777"))

        self.assertEqual(len(root.children), 1)

        resolved = root.resolve(self.bot, self.clientid)
        self.assertIsNotNone(resolved)
        self.assertEqual('<dial leave_message="true">07777777777</dial>', resolved)

    def test_to_xml(self):
        root = TemplateNode()
        xml = TemplateXMLNode()
        xml._name = "dial"
        root.append(xml)
        xml.append(TemplateWordNode("07777777777"))

        xml = root.xml_tree(self.bot, self.clientid)
        self.assertIsNotNone(xml)
        xml_str = ET.tostring(xml, "utf-8").decode("utf-8")
        self.assertEqual("<template><dial>07777777777</dial></template>", xml_str)

    def test_to_xml_with_attribs(self):
        root = TemplateNode()
        xml = TemplateXMLNode()
        xml._name = "dial"
        xml._attribs['leave_message'] = "true"
        root.append(xml)
        xml.append(TemplateWordNode("07777777777"))

        xml = root.xml_tree(self.bot, self.clientid)
        self.assertIsNotNone(xml)
        xml_str = ET.tostring(xml, "utf-8").decode("utf-8")
        self.assertEqual('<template><dial leave_message="true">07777777777</dial></template>', xml_str)
