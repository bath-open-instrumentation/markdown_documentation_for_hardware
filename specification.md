# The DocuBricks specification, annotated and updated a bit:

The root tag is `<docubricks>` which contains a number of sub-tags, detailed below.  Each of these tags has a set of allowed sub-tags.  If the tag is identified as a "(string)" the tag has no attributes, and the value is stored as the text contents of the tag.  Tag contents must be plain text, unless specified as "(safe HTML)" in which case markup is permitted.

## `<author>` tag
This describes one author, who may be referenced by ID from bricks.
### Attributes
* `id` (string): an ID number/string for the author
### Child tags
* `<name>` contains the author's name
* `<email>` contains the author's email
* `<orcid>` contains an ORCID ID
* `<affiliation>` contains the author's affiliation.  Should multiple affiliations be allowed?

## `<part>` tag
### Attributes
* `id` (string): an ID number/string that's used to identify the part
### Child tags
* `<name>` (string) the name/title of the part
* `<description>` (safe HTML) a longer description
* `<supplier>` (string)
* `<supplier_part_num>` (string)
* `<manufacturer_part_num>` (string)
* `<url>` (string) link to an internet source of the part
* `<material_amount>` (string)
* `<material_unit>` (string)
*  `<media>` contains:
    * `<file url=""\>` tags, where the `url` attribute links to images, videos, CAD files, and more
* `<manufacturing_instruction> describes how the part is made contains: 
    * `<step>` tags, each describing one step of the instructions, containing:
        * `<description>` (string)
        * `<media>` (see above, contains `<file>` elements)

## `<brick>` tag
### Attributes
* `id` (string): an ID number/string that's used to identify the brick
* `<name>` (string) the name/title of the part
* `<abstract>` (safe HTML) a short description
* `<long_description>` (safe HTML) a longer description
* `<notes>` (safe HTML)
* `<media>` (see above, contains `<file>` elements)
* `<license>` (string)
* `<author>` tags (more than one may be present), containing the id as the text contents
* `<function>` tags (more than one allowed) refer to the roles played by required parts or bricks.  The distinction between "functions" and "implementations" is confusing, normally each function contains one implementation, and the description of the function is the title of the part or brick referenced in the implementation.  However, it can be used to group together related parts, or even to indicate alternatives.  This probably ought to be specified more tightly...  The tags contain:
    * `<description>` (string) name of the function
    * `<implementation>` tags (usually 1, but may have 0 or several).  Implementations refer to exactly one `<part>` or `<brick>` that fulfils (or part-fulfuls) the function inside which the tag is placed.  These have no sub-tags, but several attributes:
        * `type` ("brick" or "part")
        * `id` (string) of the brick or part respectively
        * `quantity` (string) how many pieces of this implementation are needed
* `<assembly_instruction>` describes how the assembly is put together, and contains: 
    * `<step>` tags, each describing one step of the instructions, containing:
        * `<description>` (string)
        * `<media>` (see above, contains `<file>` elements)
        * `<component>` tags (optional, may have several) contain the id of functions of the brick needed in this assembly step.
* `<custom_instruction> adds another set of instructions, which may be calibration, testing, etc. - there is a `type` attribute (or should this be a sub-tag?) specifying the meaning of the custom instructions.  This contains: 
    * `<step>` tags, each describing one step of the instructions, containing:
        * `<description>` (string)
        * `<media>` (see above, contains `<file>` elements)
        * `<component>` tags (optional, may have several) contain the id of functions of the brick needed in this assembly step.