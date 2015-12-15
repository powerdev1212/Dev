from .abstracts import (
    AbstractMini,
    AbstractStandard,
    AbstractStandardAPIFeatured,
    AbstractRanked,
    AbstractRankedAPIFeatured,
    AbstractStringSlot,
    AbstractTextSlot,
    AbstractSmallTextSlot
    )
    
""" If django-ckeditor installed only. """
try:
    from .abstracts import AbstractRichTextSlot, AbstractSmallRichTextSlot
except:
    pass


from .adminmodels import APIFeaturedModelAdmin
