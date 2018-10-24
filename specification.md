# Title of the brick (or part)

## Authors

author id(string):
  name (string)
  email (string)
  orcid (string)
  affiliation (string)

part id(string):
  name (string)
  description (string)
  supplier (string)
  supplier_part_num (string)
  manufacturer_part_num (string)
  url (string) link to an internet source of the part
  material_amount (string)
  material_unit (string)
  media: file(s) (url) images, videos, CAD files, and more
  manufacturing_instruction: step(s): step by step instructions
      description (string)
      media: file(s) (url) (NB the url is a property of the file, not a sub-element)

brick id(string):
  name (string)
  abstract (string)
  long_description (string)
  notes (string)
  media: file (url)
  license (string)
  author(s) (id(string))
  function(s) (id(string)):
      description (string) name of the function
      implementation(s) (type(“brick” or “part”), id(string) of brick or part respectively, quantity (string) how many pieces of this implementation are needed)

  assembly_instruction: step(s): step by step instructions
      description (string)
      media: file(s) (url)
      component(s) (id(string) of function) local reference to functions in the brick needed as component in this assembly step

  custom_instruction(s) type(string): step(s): other step by step instructions of custom type e.g. safety, testing, calibration, user_manual, improvement_suggestions, etc.
      description (string)
      media: file(s) (url)