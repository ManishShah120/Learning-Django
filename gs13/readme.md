# Django Template Language(DTL) Crash Course
- Filters `{{variable|filter_name}}`
- Template Tags
    - `if` Tag
        - `{% if variable %}`
        - `{% endif%}`

    - `if` Tag with filter
        - `{% if nm|length >=6 %}`
    
    - `and` operator
        - `{% if nm and st %}`

    - `for` loop
        - `{% for object in objects %}`
        - `{% endfor %}
    
    - Predefined `forloop` variable
        - `forloop.counter`
        - `forloop.counter()`
        - `forloop.revcounter` reverse counter
        - `forloop.revcounter()`
        - `forloop.first`
        - `forloop.last`
        - `forloop.parentloop`
