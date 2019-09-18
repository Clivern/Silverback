"""
    Error Web Controller
    ~~~~~~~~~~~~~~

    :copyright: silverbackhq
    :license: BSD-3-Clause
"""

# Standard Library
import os

# Third Party Library
from django.shortcuts import render
from django.utils.translation import gettext as _

# Local Library
from app.modules.core.context import Context
from app.modules.util.helpers import Helpers


def handler500(request, exception=None, template_name='templates/500.html'):
    correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
    helpers = Helpers()
    logger = helpers.get_logger(__name__)

    if exception is not None:
        logger.error("Server Error: %(exception)s {'correlationId':'%(correlationId)s'}" % {
            "exception": exception,
            "correlationId": correlation_id
        })

    template_name = 'templates/500.html'

    context = Context()

    context.autoload_options()
    context.push({
        "page_title": _("500 · %s") % context.get("app_name", os.getenv("APP_NAME", "Silverback"))
    })

    return render(request, template_name, context.get(), status=500)
