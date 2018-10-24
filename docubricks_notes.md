# Markdown-based hardware documentation

I've been involved with DocuBricks since near the beginning, and I'm really keen on what it aims to do - there is clearly a need for an open standard for hardware documentation.  The current XML format has a lot of good features, and I reckon it does a very good job of capturing the correct information.  However, there are a number of problems that have led to various projects I've been involved with choosing not to adopt it.  Mainly, these are:

* Difficulties using/obtaining the editor, or getting the right version - sadly people tend to give up quite quickly if it's not immediately clear where to go or what to do.
* The Java editor/viewer has no support for formatting or hyperlinks, which limits the usefulness, and can make it hard to structure the instructions.
* Docubricks.com doesn't let you edit/version projects, which gets problematic.
* The XML format is not human-readable and, even with explanatory notes, it's not obvious how to edit it.
* There is heavy use made of long, random-looking strings as ID numbers, which make it hard to see what's being referred to (e.g. parts, bricks, etc.).

Irrespective of ones opinion on Docubricks.com (I'm suggesting that's a separate discussion), the idea of an open format for hardware documentation is a very useful one.  I'd like to suggest replacing the XML format with something based on Markdown.  This has a number of advantages:

* Documentation would be human-readable and editable in familiar web interfaces or text editors (think Wikipedia).
* There are loads of tools available to render, manipulate, parse, and edit markdown.
* Easy rendering to HTML is possible with e.g. Jekyll, and it can be easily extended to parse out a BOM, etc.
* All of the information contained in DocuBricks can be easily ported.
* A one-file-per-brick format would make it easier to navigate without a specialist editor.

Together with a couple of colleagues here (Julian and Joel) we're likely to look into the technical feasibility of this, but we're quite confident.  We will then start putting together some sort of specification.  We're not currently calling what we are working on Docubricks, but I'm keen to make sure it's compatible, and to avoid pointless duplication.  Longer-term it would be good to look into how such a format could become a standard (with all the implications that has for governance and shared ownership) but for the short term, I think we will focus on figuring out a specification that makes sense, and a minimal implementation of a renderer (ideally one which replicates the features of DocuBricks but with much, much less bespoke code).

One quite high-priority feature is the ability to preview what we're doing, and to render it from a repository (e.g. Github).  That doesn't mean we're against archival in a dedicated repository (like DocuBricks) but that we'd prefer to have a viewable working copy as well.  The model adopted by Kitspace (where projects live on e.g. github/gitlab and are then rendered on their website with value-added features) is one I really like.
