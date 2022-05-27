class Script:
    """A collection of actions.

    The responsibility of Script is to keep track of a collection of actions. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actions (dict): A dictionary of actions { key: group_name, value: a list of actions }
    """

    def __init__(self):
        """Construct a new instance of Script."""
        self._actions = {}

    def add_action(self, group, action):
        """Add an action to a group.
        Args:
            group (str): The name of the group
            action (Action): An instance of Action
        """
        if group not in self._actions:
            self._actions[group] = []
        if action not in self._actions[group]:
            self._actions[group].append(action)

    def get_actions(self, group):
        """Get all actions from a group
        Args:
            group (str): The name of the group
        Return:
            results (list): A list of actions
        """
        results = []
        for action in self._actions[group]:
            results.append(action)
        return results

    def remove_action(self, group, action):
        """Remove an action from a group.
        Args:
            group (str): The name of a group
            action (Action): An instance of Action
        """
        if group in self._actions:
            if action in self._actions[group]:
                self._actions[group].remove(action)