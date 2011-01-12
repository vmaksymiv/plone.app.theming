PROFILE='profile-plone.app.theming:default'

def upgrade_10a1_to_1002(context):
    #registry
    setup = context.runImportStepFromProfile(PROFILE,
        'plone.app.registry',
        purge_old=False)
