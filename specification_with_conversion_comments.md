# The DocuBricks specification, annotated and updated a bit:

The root tag is `<docubricks>` which contains a number of sub-tags, detailed below.  Each of these tags has a set of allowed sub-tags.  If the tag is identified as a "(string)" the tag has no attributes, and the value is stored as the text contents of the tag.  Tag contents must be plain text, unless specified as "(safe HTML)" in which case markup is permitted.

## `<author>` tags *are in-lined into the bricks that reference them*
This describes one author, who may be referenced by ID from bricks.
### Attributes
* `id` (string): an ID number/string for the author
### Child tags
* `<name>` contains the author's name
* `<email>` contains the author's email
* `<orcid>` contains an ORCID ID
* `<affiliation>` contains the author's affiliation.  Should multiple affiliations be allowed?

## `<part>` tag
*Each part becomes one markdown file.  Initially I've separated them out into a "parts" folder but I'm not convinced this distinction is really necessary.*
### Attributes
* `id` (string): an ID number/string that's used to identify the part *The ID is abolished an replaced with the filepath, relative to the root of the documentation*
### Child tags
* `<name>` (string) the name/title of the part *the first top-level heading*
* `<description>` (safe HTML) a longer description *the text between the title and the metadata below*
* `<supplier>` (string) *Part of the metadata microformat (YAML, table, or unordered list?)*
* `<supplier_part_num>` (string) *as above*
* `<manufacturer_part_num>` (string) *as above*
* `<url>` (string) link to an internet source of the part *as above*
* `<material_amount>` (string) *as above*
* `<material_unit>` (string) *as above*
* `<media>` contains: *media blocks are a sub-section containing an unordered list*
    * `<file url=""\>` *converted to markdown links, either `![](url)` or `[[url]]` without the `!` depending on the format?*
* `<manufacturing_instruction> *a top-level section*
    * `<step>` *a second-level section (`##`)*
        * `<description>` (string) *the text of the section*
        * `<media>` (see above, contains `<file>` elements) *as above, but now a `###` section*

## `<brick>` tag
*Each brick becomes one markdown file in the top level of the documentation*
### Attributes
* `id` (string): *abolished in favour of filename*
* `<name>` *first top level heading*
* `<abstract>` *first paragraph of text*
* `<long_description>` *all text following the heading*
* `<notes>` *a top-level section called "Notes"*
* `<media>` *a subsection of the first top level heading (i.e. between the first and second `#` headings)*
* `<license>` (string) * An item in the metadata list (as for part)*
* `<author>`  * An item in the authors list (as for part metadata)*

* `<function>` tags *become list items in the "Requirements" subsections*
    * `<description>` *is the text of the item*
    * `<implementation>` tags *become links in the list item*
        * `type` ("brick" or "part") *There are subsections for "assemblies" and "parts", the `type` attribute determines where things go.  Any function that has at least one implementationt hat is a brick ends up in the "assemblies" list.*
        * `id` (string) *is converted to a hyperlink*
        * `quantity` *is currently ignored in favour of the `quantity` in the function??*
        
* `<assembly_instruction> *becomes a top level section as for part manufacturing instructions* 
    * `<step>` tags, each describing one step of the instructions, containing:
        * `<description>` (string)
        * `<media>` (see above, contains `<file>` elements)
        * `<component>` tags *become links somewhere in the step?*
* `<custom_instruction> *becomes another top level section, with the title derived from the `type` attribute.