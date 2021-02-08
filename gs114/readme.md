# View Class Based View or View Base Class

## View Class-Based Base View
- Function Based View
- Class Based View ✅

### Class Based View
Class-based views provide an alternative way to implement views as Python objects instead of functions.

Two Types:-
- Base Class-Based Views / Base View
- Generic Class-Based Views / Generic View
 

#### Base Class-Based Views / Base View
We get 3 classes in this view:-
- View
- TemplateView
- RedirectView
##### View
`django.views.generic.base.View`
<u>Attributes:-</u>
`http_methods_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace']`
<u>Methods:-</u>
- `setup(self, request, *args, **kwargs)`
- `dispatch(self, request, *args, **kwargs)`
- `http_method_not_allowed(self, request, *args, **kwargs)`
- `options(self, request, *args, **kwargs)`
- `as_view(cls, **initkwargs)`
- `_allowed_methods(self)`
