# Q Object

from django.db.models import Q

-   - & (AND) Operator
-   - Eg.:- Student.objects.filter(Q(id=6) & Q(roll=106))

-   - | (OR) Operator
-   - Eg.:- Student.objects.filter(Q(id=6) | Q(roll=108))

-   - ~ Negation Operator
-   - Eg.:- Student.objects.filter(~Q(id=6))
