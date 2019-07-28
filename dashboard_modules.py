from jet.dashboard.modules import DashboardModule

# Test custom module.
class Test(DashboardModule):
    title = 'Test Module'
    title_url = "google.com"
    #Ticket.get_admin_changelist_url()
    template = 'custom_jet_modules/test.html'

    def init_with_context(self, context):
        pass
