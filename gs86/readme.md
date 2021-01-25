# Template Fragment Caching

## Template Fragment Caching[File System based Caching]

### More control what to cache
- {% load cache %} [Gives the access to cache tag in template]
- {% cache %} [Caches the contents of the block]
    Syntax:
        {% cache timeout name variable using="" %} ... {% endcache name %}
    Example
        {% cache 60 sidebar request.user.username using="localcache" %}
            ..sidebar for logged in user ...
        {% endcache %}
