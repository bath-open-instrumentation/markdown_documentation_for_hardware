"""
This is a Python 3 script to convert the microscope XML documentation into markdown
"""

import xml.etree.ElementTree as ET
import sys
import os
import shutil
import re
import time

def namify(title):
    """Replace spaces with underscores etc. to generate sensible filenames from titles"""
    name = title.replace(" ","_") # replace spaces with underscores
    name = re.sub(r'\W+', '', name) # strip non-alphanumeric chars (allows '_')
    return name.lower()
    
def html_strip(html, pad_l=True, pad_r=True, none_to_empty_string=True):
    """Replace leading or trailing whitespace with a single space.
    
    HTML is whitespace-insensitive-ish, in that any amount of whitespace becomes one space.
    When converting to markdown, it is useful to respect this, hence this function.
    If there is any leading or trailing space, that whitespace is replaced with a single
    space.  Set ``pad_l`` or ``pad_r`` to ``False`` to disable adding the extra space.
    
    TODO: decide if this function should just do a re.sub("\s+", " ") to replace **all** whitespace
    """
    if html is None and none_to_empty_string:
        html = ""
    lstripped = html.lstrip()
    if len(lstripped) < len(html) and pad_l:
        lstripped = " " + lstripped
    stripped = lstripped.rstrip()
    if len(stripped) < len(lstripped) and pad_r:
        stripped += " "
    return stripped
    
def safe_html_to_markdown(element, prefix="", recursion_count=0, links_to_convert={}):
    """Take an XML Element and turn its contents into MarkDown, respecting safe HTML tags.
    
    For this function, "safe" HTML tags are ["b","i","ul","ol","li","p","a","pre","code"]
    This function is **NOT production-ready** or guaranteed in any way.  It should make a
    decent stab at converting, but I have not handled all edge cases!
    
    Arguments:
        prefix: string (optional, default "")
            This string will be prefixed to every line output, which allows nested lists etc.
        recursion_count: (integer, default 0)
            The recursion count is used internally to avoid infinite loops
    """
    assert recursion_count < 100, "Exceeded maximum recursion depth converting HTML to markdown"
    rargs = {"recursion_count":recursion_count + 1, "links_to_convert":links_to_convert}
    md = html_strip(element.text, pad_l=False) # Start with the text immediately following the opening tags
    inlines = {'b':'**', 'strong':'**', 'em':'*', 'i':'*', 'code':'`', 'u':"__"}
    lists = {'ul':'*   ', 'ol':'1.  '}
    for e in element:
        tag = e.tag.lower()
        if tag in inlines: # Handle emphasis (b/i/em/strong/u) and code
            md += inlines[tag] + safe_html_to_markdown(e, prefix, **rargs) + inlines[tag]
        if tag in lists: # Lists are more complicated - we add an appropriate prefix to each <li>
            for item in e:
                if item.tag.lower() == "li":
                    md += "\n" + prefix + lists[tag] + safe_html_to_markdown(item, prefix + "    ", **rargs)
            md += "\n" + prefix
        if tag == 'p':
            md += "\n" + prefix + safe_html_to_markdown(e, prefix, **rargs) + "\n\n" + prefix
        if tag == 'br':
            md += "\n\n" + prefix
        if tag == "pre":
            #TODO: think about what happens to tags in here (though DocuBricks doesn't permit them anyway)
            # Currently, we use `"".join(e.itertext())` to strip the tags out and get some text.
            md += "\n"
            for line in "".join(e.itertext()).split("\n"):
                md += "\n" + prefix + "   " + line
            md += "\n\n" + prefix
        if tag == "a":
            href = e.attrib['href']
            if href in links_to_convert:
                href = links_to_convert[href]
            md += "[" + safe_html_to_markdown(e, prefix, **rargs) + "](" + href + ")"
        md += html_strip(e.tail) # append any text that happens after the current tag
    return md
        
def step_by_step_instructions(element, sectionlevel="##", to_markdown=safe_html_to_markdown):
    """Render a <StepByStepInstruction> hierarchy to markdown"""
    output = ""
    for step in element:
        assert step.tag.lower() == "step", "instructions sections can only contain steps"
        output += sectionlevel + " Step\n"
        output += to_markdown(step.find("description"))
        output += "\n"
        output += media_section(step)
    output += "\n"
    return output
        
def media_section(element, title="Media", sectionlevel="###"):
    """Extract the <media> section and display as a list of images"""
    output = ""
    if element.find("media"):
        media_files = element.find("media").findall("file")
        if len(media_files) > 0:
            output += sectionlevel + " " + title + "\n"
            for f in media_files:
                output += "*   ![](" + f.attrib["url"] + ")\n"
    output += "\n"
    return output
        
if __name__ == "__main__":
    doc = ET.parse("./openflexure microscope.docubricks.xml")
    root = doc.getroot()

    output_folder = "./output"
    if os.path.exists(output_folder) and os.path.isdir(output_folder):
        shutil.rmtree(output_folder)
        time.sleep(0.1) # without this, Windows barfs and you have to run the script twice...

    os.mkdir(output_folder)
    os.mkdir(os.path.join(output_folder, "parts"))
    
    # We want to convert links to point to the new files, so we do a first pass to figure out the conversion
    brick_id_to_name = {}
    for brick in root.iter("brick"):
        brick_id_to_name[brick.attrib['id']] = namify(brick.find("name").text)
        
    part_id_to_name = {}
    for e in list(root.iter("physical_part")) + list(root.iter("part")):
        name = e.find("name")
        if name is None:
            name = e.find("description")
        part_id_to_name[e.attrib['id']] = namify(name.text)
        
    links_to_convert = {}
    for id, name in brick_id_to_name.items():
        links_to_convert["#brick_" + id] = name
    for id, name in part_id_to_name.items():
        links_to_convert["#part_" + id] = name
    def to_markdown(element):
        return safe_html_to_markdown(element, links_to_convert=links_to_convert)
       
    for brick in root.iter("brick"):
        title = brick.find("name").text
        name = brick_id_to_name[brick.attrib['id']]
        with open(os.path.join(output_folder, name + ".md"), "w") as file:
            file.write("# " + title + "\n")
            
            if brick.find("abstract"):
                file.write("" + to_markdown(brick.find("abstract")) + "\n\n")
            if brick.find("long_description"):
                file.write("" + to_markdown(brick.find("long_description")) + "\n\n")
                
            if brick.find("assembly_instruction") is not None:
                file.write("# Assembly Instructions\n")
                file.write(step_by_step_instructions(brick.find("assembly_instruction"), to_markdown = to_markdown))
                    
    parts = list(root.iter("physical_part")) + list(root.iter("part"))
    for part in parts:
        title = part.find("description").text
        name = part_id_to_name[part.attrib['id']]
        with open(os.path.join(output_folder, "parts", name + ".md"), "w") as file:
            file.write("# " + title + "\n")
            
            file.write(media_section(part, sectionlevel="##"))
            
            if part.find("manufacturing_instruction") is not None:
                file.write("# Manufacturing Instructions\n")
                file.write(step_by_step_instructions(part.find("manufacturing_instruction"), to_markdown = to_markdown))
    
        
                
            
            
