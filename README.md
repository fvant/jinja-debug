# jinja-debug
Debug message filter for jinja/Ansible

This custom jinja2 filter can be used to output messages to stdout while evaluating templates without adding anything to the template result, it is invisble.

```jinja
{% if foo %}
  {{ "foo is true" | debug }}
  .... 
{% endif %}
```

# Use case
The need for this filter came from using Ansible + jinja templates in recent projects. Outputting messages from the Ansible playbook was easy but trying to figure what happened (went wrong) inside a `template: ` block was impossible.
With this filter you can add good old print() messages whereever needed, assuming the template still parses of course. 

I have another repo with tests to catch potential parsing errors: it can validate parsing of a .j2 file without using Ansible but it knows about the Ansible provided filters.

## Examples
- output typical debug messages like 
```jinja
{% if foo %} 
  {{ "foo is true" | debug }}
  ....
{% endif %}
```
- show item being processed in a loop
```jinja
{% for foo in bar %} 
  {{ ("working on: " + foo) | debug }}
  ....
{% endfor %}
```
- add seperator lines to output
```jinja
{{ ("----------") | debug }}
``` 
- output the size of a string (for example the user_data script for an EC2)
```jinja
{{ ( "Size of my script: " + ( "#!/bin/bash \n my bash script" | string | count | string) ) | debug }}
``` 

# Ansible installation
The file `debug.py` should be copied to the folder with the filter plugins, typically `./filter_plugins` and it is ready for use right away.
