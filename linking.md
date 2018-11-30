# Linking between pages

The way individual markdown pages link together is probably the most important thing to get right - in particular, because it will determine how we put together a bill of materials, and how we serialise the (tree-based) structure of the markdown files into something that can be easily printed or downloaded in a single file.  There are a number of ways in which links are likely to be used:

*   References/further information on external URLs, i.e. "regular" hyperlinks.  It might be sensible to open these in another window/tab, as they are not part of the instructions.  This is definitely true when working in some sort of editor, online or offline. (e.g. "for more information, see [telecentric imaging](https://wikipedia.org/telecentric_imaging).")
*   Referring to other parts of the instructions
    -   in an "informational" way (e.g. "it's like [this step]")
    -   to indicate layout/sequence/order (e.g. "now move on to [assemble the next thing]")
    -   to indicate a requirement for a part or sub-assembly (e.g. "insert the two [m3 screws](parts/m3_screw){qty consumed:2}")

For informational links (the first two cases) there's probably nothing special needed; in the case of internal links it might be nice to display some sort of sensible mouse-over preview with a thumbnail image.  That's particularly nice when referencing parts, as it makes it easy to figure out which is which.  However, that's a feature that can be entirely implemented in the viewer and doesn't need anything from the file format.

Links that indicate sequence could probablay do with explicit markup to show that - and it may be that simply including a "previous" or "next" page in a YAML block at the top of the file would make it clearer.  It's possible that in some cases, the right thing to do is to "embed" one page in another - that is not without its tricky issues, but it might be worth at least making provision for that being included in a future version.  I'd envisage a collapsible block that lets you expand it for more information.  That would be useful if you need to add more detail on a particular assembly step, but don't want to clutter the main file (we should probably define a section that gets removed, which can be used to explain to someone stumbling across that file in isolation that it's meant to be embedded, like `## Embedded file`).

## Requirements links (practical version)
One of the most important goals of this project is to allow for some computer assistance in managing the bill of materials.  We propose to represent each part with a link, and to indicate extra information like quantities using a curly-bracket YAML block immediately after the link.  There are three syntaxes likely to be useful:

* `[some screw](parts/some_screw){qty: 4} indicates that you need four of the screw.  This link can appear anywhere in the file.
* `[some screw](parts/some_screw){total_qty: 7} indicates that you need a total of 7 screws to make everything described in this file.  NB a helpful viewer/editor should warn you if you have a total quantity that doesn't match the sum of the other links on the page.
* `[a screwdriver](tools/screwdriver){type: tool}` indicates that you need a screwdriver - you can do this several times in the file, it won't assume you need more than one screwdriver unless you specify `{qty: 2, type: tool}` (to indicate you need two of them) or you use `{qty: 2, type: part}` (to indicate that the screwdriver is becoming part of the assembly)

## Requirements links (in more detail)
Links that indicate requirements are most important - these are what we would use to put together a bill of materials.  It's therefore important to get the markup on these right!  We propose adding a suffix to the link enclosed in curly brackets.  Curly brackets are escapable in markdown, but not used by any of the core markdown implementations.  The content of the curly brackets should be parsable as YAML, perhaps with something at the start to indicate that it's specific to the hardware documentation format - e.g. the first item could indicate that what follows is for the bill of materials.  Bills of materials are not quite as simple as just adding up all the quantities - there are some items that can be re-used (like tools) and some items that get consumed and/or become a part of the thing you're building (like electronic components or screws).  To handle this, we propose using a "type" parameter.  Different types can be added up in different ways, with the possibility to define custom types in some as-yet-not-written syntax.  A link with bill-of-materials information should look like a markdown link (any valid syntax for the markdown link is OK) followed by a YAML block, that defines a "hash" (key-value pairs) with a `qty` key and a `type` key.

By default, there are two types:

### Type parameter
When a link includes bill-of-materials metadata, 

*   **part** is the default type (what you get if you don't specify a type explicitly).  It is added up with simple summation, i.e. you add up all the quantities to get the total for the file.  That means if you use one screw in each of 5 assembly steps, each time saying `now attach the widget with a [screw](parts/my_screw){qty: 1}`, the bill of materials for your file will have 5 screws in it.
*   **tool** is another type, with the total for the file being the maximum quantity specified.