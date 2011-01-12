from zope import interface
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.schema.interfaces import ITextLine

_ = MessageFactory(u"plone")

THEME_RESOURCE_NAME = 'theme'
RULE_FILENAME = 'rules.xml'
MANIFEST_FILENAME = 'manifest.cfg'

class IThemeSettings(interface.Interface):
    """Transformation settings
    """
    
    enabled = schema.Bool(
            title=_('enabled', u"Enabled"),
            description=_('enable_theme_globally',
                          u"Use this option to enable or disable the theme "
                          u"globally. Note that the options will also affect "
                          u"whether the theme is used when this option is "
                          u'enabled.'),
            required=True,
            default=False,
        )
    
    rules = schema.TextLine(
            title=_('rules_file', u"Rules file"),
            description=_('rules_file_path',
                          u"File path to the rules file"),
            required=False,
        )
    
    absolutePrefix = schema.TextLine(
            title=_('absolute_url_prefix', u"Absolute URL prefix"),
            description=_('convert_relative_url',
                 u"Convert relative URLs in the theme file to absolute paths "
                 u"using this prefix."),
            required=False,
        )
    
    readNetwork = schema.Bool(
            title=_('readNetwork', u"Read network"),
            description=_('network_urls_allowed',
                          u"If enabled, network (http, https) urls are "
                          u"allowed in the rules file and this config."),
            required=True,
            default=False,
        )

class IDomainToTheme(interface.Interface):

    domainsToTheme = schema.List(
            title=_('label_domainsToTheme',
                    default=u'Domains to theme'),
            description=_('help_domainsToTheme',
                          default=u"Add domains whith theme id."),
            value_type=schema.TextLine(
                title=_('Domain to theme'),
            )
        )

class IThemingLayer(interface.Interface):
    """Browser layer used to indicate that plone.app.theming is installed
    """
