from django.test import TestCase


class LoadersTest(TestCase):

    def test_asco_loader(self):
        from experts import handlers as exh
        from . import models as lem

        engine = lem.LoaderEngine.objects.get(mnemo="asco", active=True)
        handler = exh.ASCOUploadHandler(
            **{k: v for k, v in engine.config.__dict__.iteritems()}
            )
        handler.format_url()
        print handler._curr_url
