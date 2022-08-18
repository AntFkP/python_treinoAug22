import xml.dom.minidom  

def manipulaXML():
    doc = xml.dom.minidom.parse("exemploXML.xml")  # criar um objeto 

    print("Nome da primeira tag: ", str(doc.firstChild.tagName))
    primeiroNome = doc.getElementsByTagName("firstname")
    print("O primeiro nome é: ", primeiroNome[0].firstChild.nodeValue)

    for skill in doc.getElementsByTagName("skill"):  # conteudo de todas as tags com o nome skill
        print("Skill encontrado: " , skill.getAttribute("name"))

manipulaXML()