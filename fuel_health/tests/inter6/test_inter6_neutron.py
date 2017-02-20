import logging

from fuel_health import neutronmanager

LOG = logging.getLogger(__name__)


class NeutronApiTests(neutronmanager.NeutronBaseTest):
    """TestClass contains tests that check basic Ceilometer functionality."""

    def test_check_agents(self):
        """Neutron test to check agents
        Target component: Neutron

        Scenario:
            1. Request the list of agents.
            2. Check agents alive.

        Duration: 20 s.
        Deployment tags: neutron
        """

        fail_msg = 'Failed to get list of agents.'
        response = self.verify(60, self.neutron_client.list_agents,
                               1, fail_msg, 'getting list of agents')

        for agent in response['agents']:
            self.verify_response_true(agent['alive'],
                                      'Step 2 failed: On the {0}, {1} is not alive.'
                                      .format(agent['host'], agent['binary']))
