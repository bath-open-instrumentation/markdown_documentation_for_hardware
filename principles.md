# Design ideas for a hardware documentation format

This repository is about figuring out some conventions that will allow us to nicely document hardware using a markdown-based lanugage.  The key ideas are:
* It should **be as human-readable as possible.**  That makes it easy for people to contribute (all you need is a text editor), and it plays nicely with web editors and viewers.
* It should **render nicely as markdown** so that it's possible to view it in a prettier format than text-only, but without requiring any specific software.
* It should **leave room for extension/adaptation** to allow for things we've not thought of
* It will **be an open format** that isn't restricted by copyright/IP/whatever
* There should be **sensible linking** between sections/assemblies/parts, within a project and between projects.
* We should make provision for **machine-readable bills-of-materials** to help projects like kitspace make it easy to get hold of the hardware

## Structure
It would be nice to have some flexibility in the structure of documentation.  It's often nice to try to describe a piece of hardware hierarchically, because that lends itself to being modular and having dependencies.  However, it's usually more natural to describe how to build something as a narrative.  One approach to this is having a way of describing the order in which the components should be presented (e.g. you could have an introduction, followed by the bill of materials, followed by the sub-assemblies you need to make, followed by the main assembly steps in order).  It seems to me that having an introduction, followed by a requirements-first ordering of things?  A bit of customisation potential would certainly be handy...

