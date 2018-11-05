# Design ideas for a hardware documentation format
There are plenty of ways to document a piece of hardware, but currently no specific file format for exchanging information between them.  There are some common features of hardware documentation that go beyond the provision of a standard word processor, and it would be good to make sure these are provided by a simple, open format.  Specifically, things which are needed are:
* **Step by step instructions** for assembly, testing, use, etc.
    * Each step usually has a number of **images or other media files** associated, and it would be good to have a standard way to display these along with the text for a step.
    * It's important to be able to **link and cross-reference** other parts of the instructions, and/or external resources.
    * It would be nice to be able to specify **parts/components/tools** used by each step.
* A **bill of materials** is an important part of any hardware project.  Making it as easy as possible to find the component parts of a project really helps people to replicate it.
    * It would be great to encourage people to **include as much information as possible** to allow parts to be sourced anywhere in the world.
    * Ideally, it would be good to make this **machine-readable**, enabling services like [KitSpace](http://www.kitspace.org) to supply kits with low overheads.
    * The ability to reference **standard parts** would be very helpful - perhaps these could live in an online repository.  It would be good to avoid the need to centralise this repository.
* Reasonable **printable/offline format** because often hardware projects are built in the lab, or at a workshop, and it's good not to have to rely on online resources.
    * Provision for a tool that automatically **embeds or caches remote requirements** (such as parts that live in a repository somewhere else) would be really helpful.

The features above should, ideally, be used in a way that limits the authors as little as possible - while modular, re-usable documentation is great, it should not come at the expense of readability.  The use of sections, chapters, etc. etc. should be left as something the author of the documentation can choose.

This repository is about figuring out some conventions that will allow us to nicely document hardware using a markdown-based lanugage.  The key ideas are:
* It should **be as human-readable as possible.**  That makes it easy for people to contribute (all you need is a text editor), and it plays nicely with web editors and viewers.
* It should **render nicely as markdown** so that it's possible to view it in a prettier format than text-only, but without requiring any specific software.
* It should **leave room for extension/adaptation** to allow for things we've not thought of
* It will **be an open format** that isn't restricted by copyright/IP/whatever
* There should be **sensible linking** between sections/assemblies/parts, within a project and between projects.
    * This linking should make provision for **machine-readable bills-of-materials** to help projects like kitspace make it easy to get hold of the hardware
* We should **avoid being prescriptive** about structure and content as much as possible - the emphasis should be on supporting good documentation rather than forcing people to do things in a particular way.
* Automatic generation of things like bills of materials should **help but not force** the author - e.g. by allowing them to specify quantities in different places (rather than auto-counting how many parts you need) and then warning the author if those quantities don't add up correctly.  Similarly, if a structure for the table of contents makes sense to the author, they should be able to specify it without being tied to an auto-generated tree (though the latter is fine if the author doesn't want to do it).

## Structure
It would be nice to have some flexibility in the structure of documentation.  It's often nice to try to describe a piece of hardware hierarchically, because that lends itself to being modular and having dependencies.  However, it's usually more natural to describe how to build something as a narrative.  One approach to this is having a way of describing the order in which the components should be presented (e.g. you could have an introduction, followed by the bill of materials, followed by the sub-assemblies you need to make, followed by the main assembly steps in order).  It seems to me that having an introduction, followed by a requirements-first ordering of things?  A bit of customisation potential would certainly be handy.  Some example use cases would help:

### Simple projects
The simplest case is of a project that has one sequence of instructions.  These are quite common, and the structure doesn't take a lot of thought:
* Title & introduction
* Bill of materials
* Step by step instructions (including photos)
The bill of materials should reference more information on each part, but probably using a click-to-expand interface, or putting the additional details in sub-pages.

### Longer projects
If projects are a bit longer, assembly is probably split up into stages.  Perhaps it makes sense to adopt a book-like structure, with "chapters" (which are probably individual files).  Each chapter can have its own bill of materials (which may or may not be displayed) and the whole project probably needs an introduction with a master BoM at the start.  It would be nice to be able to specify the layout independently from the dependencies of each chapter on parts and other chapters (probably each chapter depends on the previous one, but that's not given).

### Multi-part projects
Where there is a component (sub-assembly, module, call it what you will) it would be nice to make it easy to chop that out and re-use or reference it elsewhere.  That implies that putting it in a separate file would be convenient.  Some projects might be conceieved as a "tree" of assemblies, each of which is broken down into smaller parts.  In these cases, that tree could be represented by the sub-assemblies appearing in bills of materials of the larger assemblies.  That's fine for an online format, but it's worth thinking about how that might be serialised for assembly (which usually happens in a linear fashion).  Equivalently, a printed document has to have some sort of order (even if the builder chooses not to follow it) and it might be nice to allow the author to specify this.



