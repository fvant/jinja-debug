# jinja-debug
Debug message filter for jinja/Ansible

This custom jinja2 filter can be used to output messages to stdout while evaluating templates without adding anything to the template result, it is invisble.

```{% if foo %} {{ "foo is true" | debug }}  ....  {% endif %}```

# Use case
The need for this filter came from using Ansible + jinja templates in recent projects. Outputting messages from the Anaible playbook was easy but trying to figure what happened inside a `template: ` block was impossible.
With this filter you can add good old print() messages whereever needed, assuming the template still parses of course. 
I have another repo with tests to catch potential parsing errors, outside Ansible.

## examples
- output typical debug messages like 
```{% if foo %} {{ "foo is true" | debug }}  ....  {% endif %}```
- show item being processed in a loop
```{% for foo in bar %} {{ ("working on: " + foo) | debug }}  ....  {% endfor %}```
- add seperator lines to output
```{{ ("----------") | debug }}``` 
- output the size of a string (for example the user_data script for an EC2)
```{{ ( "Size of my script: " + ( "#!/bin/bash \n my bash script" | string | count | string) ) | debug }}``` 
