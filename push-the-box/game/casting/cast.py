class Cast():
    """A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """
    
    def __init__(self):
        """Constructs a new instance of Cast"""
        self._actors = {}

    def add_actor(self, group, actor):
        """Add an actor to the cast in the specified group.
        Args:
            group (str): The name of the group
            actor (Actor): An instance of Actor
        """
        if group not in self._actors.keys():
            self._actors[group] = []

        if actor not in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """Get all actors from a specified group within the cast.
        Args:
            group (str): The name of the group
        Return:
            actors (list): A list of actors
        """
        if group in self._actors.keys():
            return self._actors[group]

    def get_first_actor(self, group):
        """Get the first actor from a group.
        Args: 
            group (str): The name of the group
        Return:
            actor (Actor): An instance of Actor
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]

        return result

    def get_all_actors(self):
        """Get all actors in the cast.
        Return:
            actors (list): A list containing all actors
        """
        actors = []
        for group in self._actors:
            actors.extend(self._actors[group])
        return actors

    def remove_actor(self, group, actor):
        """Removes an actor from a group
        Args:
            group (str): The name of the group
            actor (Actor): An instance of Actor
        """
        if group in self._actors:
            if actor in self._actors[group]:
                self._actors[group].remove(actor)

    def remove_all_actors(self):
        """Remove all actors from the cast."""
        self._actors = {}