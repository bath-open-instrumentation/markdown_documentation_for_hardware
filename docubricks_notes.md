# Markdown-based hardware documentation

## How does this relate to docubricks?
As a result of a few discussions I've had, I am interested in finding a more human-readable representation for DocuBricks format documentation.  I've been involved with DocuBricks since near the beginning, and I'm really keen on what it aims to do - there is clearly a need for an open standard for hardware documentation.  The current XML format has a lot of good features, and I reckon it does a very good job of capturing the correct information, but it would be nice to have something that is easier to read and/or edit with only a text editor.  The obvious candidate for this seems to me to be MarkDown.  My aim is to fix a few issues that have held me and others up from documenting various projects in DocuBricks:
* The XML files are not particularly human-friendly, particularly because they are long and make heavy use of unique identifiers that are long strings of numbers and letters, with no obvious meaning.
* The Java-based editor/viewer does not yet support the formatting features I added to the HTML viewer last year
* Viewing the files requires either the Java editor, uploading to DocuBricks, or setting up the modified HTML viewer - none of these provide an instant preview
* Despite our best efforts, DocuBricks is not yet a well-known standard, and so people assume it is not editable when they see it in my Github repository.  This is possibly the biggest issue for me - it makes people feel the project is less open, despite the fact that it's specifically designed as an open standard!
* Difficulties using/obtaining the editor, or getting the right version - sadly people tend to give up quite quickly if it's not immediately clear where to go or what to do.
* The Java editor/viewer has no support for formatting or hyperlinks, which limits the usefulness, and can make it hard to structure the instructions.
* Docubricks.com doesn't let you edit/version projects, which gets problematic.
* The XML format is not human-readable and, even with explanatory notes, it's not obvious how to edit it.
* There is heavy use made of long, random-looking strings as ID numbers, which make it hard to see what's being referred to (e.g. parts, bricks, etc.).

I am interested in using MarkDown to represent the same information you get in a docubricks XML file.  I think this has a number of advantages:
* MarkDown is very human-readable, and is familiar to most people (e.g. via Wikipedia, Github, etc.)
* There are already a variety of mature, stable, high performance editors and renderers for MarkDown, many of which work very nicely in a browser.
* MarkDown would lend itself to a one-file-per-brick representation, which would be easier to navigate in a text editor
* Support for basic (safe) formatting and hyperlinks is built in
* Previews and rendering are easily introduced via projects like Jekyll, and would almost certainly play nicely with something like Electron if we wanted an offline WYSIWYG editor.
* MarkDown is a very well known standard, and with the addition of a little extra metadata (perhaps in YAML format) would be convertible to docubricks XML in either direction.
* All of the information contained in DocuBricks can be easily ported.
* A one-file-per-brick format would make it easier to navigate without a specialist editor.

Together with a couple of colleagues here (Julian and Joel) we're likely to look into the technical feasibility of this, but we're quite confident.  We will then start putting together some sort of specification.  We're not currently calling what we are working on Docubricks, but I'm keen to make sure it's compatible, and to avoid pointless duplication.  Longer-term it would be good to look into how such a format could become a standard (with all the implications that has for governance and shared ownership) but for the short term, I think we will focus on figuring out a specification that makes sense, and a minimal implementation of a renderer (ideally one which replicates the features of DocuBricks but with much, much less bespoke code).

One quite high-priority feature is the ability to preview what we're doing, and to render it from a repository (e.g. Github).  That doesn't mean we're against archival in a dedicated repository (like DocuBricks) but that we'd prefer to have a viewable working copy as well.  The model adopted by Kitspace (where projects live on e.g. github/gitlab and are then rendered on their website with value-added features) is one I really like.
