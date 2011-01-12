from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.app.theming import interfaces
from plone.z3cform import layout

class DomainsToThemeControlPanelForm(RegistryEditForm):
    schema = interfaces.IDomainToTheme

DomainsToThemeControlPanelView = layout.wrap_form(DomainsToThemeControlPanelForm,
                                                 ControlPanelFormWrapper)
