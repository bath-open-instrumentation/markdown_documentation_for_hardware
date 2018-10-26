* Basic object structure for DocuBricks
    - "Bricks" are units of instruction, which are arranged in a tree.  Each brick has:
        * A title
        * An abstract (could be a defined subsection)
        * A long_description (ditto)
        * Notes (ditto)
        * License (could be in a definition list?)
        * Some parts
        * Some other files
        * Some instructions
            - Each instruction step can reference images, parts, other files using standard syntax for hyperlinks or embedded links (the ![thing](url) syntax used for embedding images.
    - "Parts" are like bricks, but generally smaller - they pretty much share all the properties but have a few extras:
        * Supplier, part number, url, material amount/unit
    - There are other entities contained in a docubricks document
        * Authors, which have name, email, orcid and affiliation - this could be a list at the start of the document. For the sake of modularity, define the authors subsection so that it can occur in any brick and apply to all sub ricks unless overridden.
        * There is some (unused) provision for layout and document structure, at the moment the only structure is given by the order bricks appear in the XML document, and the hierarchy formed by considering which bricks are required by other bricks.
         In the case of embedded or linked media, do we want to provide control over how they are displayed? I think this probably ought to be minimal.  
        * Hyperlinks to other bricks, parts, or webpages should render as links, optionally with a pop up mouse over preview if possible (for parts or bricks)
        * Embed links to parts or bricks might show as subsections with an expand/contract widget, and maybe a fallback link.
        * Links to images, videos, STLs, or other such things should default to including them in a sidebar or media area, perhaps with a link in the text? We could have a media subsection for media that appears without a link, or ust bung them at the end? The latter appeals to me.
        * Embed links to images and the like should be embedded as in markdown.
        * If we want any more customisation, maybe farm it out to a separate markdown file and embed a link to that. Keep the docubricks content as close as possible to valid, human editable markdown.
        * I would love a format that renders STLs in an explodable view with a slider, so you can show each stage of an assembly.
         It might be good to keep track of whether parts, bricks, etc. Are “required” or simply linked to.  That could be done with a BOM section, where links are given in a list, together with quantities. The BOM could be a micro format, an unordered list where each item consists of an optional quantity, then a link to a part, brick, or other url, followed by optional free text identifying the role of that particular item. Only items in the BOM are summed up and included in the top level BOM, but a smart editor might keep track of links to items from other places and suggest them as inclusions for the BOM.

In a proposed Markdown based format, I would say:

* Each "brick" is one file
* Each part is one file
* If there's an obvious way to map features above to Markdown, we use it - e.g. the first top-level heading would be the title, we could use a section for the description/abstract, and sections to delineate steps.
* Linking between files should be handled with things that look like Markdown hyperlinks, because that will render nicely and make sense.  There are probably a number of places where it makes sense to add some information to those links - e.g. whether it's a requirement/dependency or just a link for information, and whether it should be propagated into the BoM or list of tools.  This could be done with subsections or something - e.g. have a subsection for tools, another for component parts.  Keep the entries as simple as possible (e.g. quantity and link) with details in the part file.
* A library of standard parts would be nice, but keeping it as a URL gives flexibility to update the library, etc.
* SENSORICA have an interesting system for keeping track of all this sort of linked information, might be worth a look.
