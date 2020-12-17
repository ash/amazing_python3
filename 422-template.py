# Using templates to create a string
# with placeholders.

from string import Template

t = Template('Hello, $name!')
# This is a template which you can
# use more than once

print(t.substitute(name='John'))
print(t.substitute(name='Anna'))
