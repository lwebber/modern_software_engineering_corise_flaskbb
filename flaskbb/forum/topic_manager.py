# CoRise TODO: implement a class for managing topics with in a forum
class TopicManager(object):
    def __init__(self, user, topics) -> None:
        self.__user = user
        self.__topics = topics

    def set_lock_state(self, desired_state):
        return self.__set_field_state('locked',desired_state)

    def set_important_state(self, desired_state):    
        return self.__set_field_state('important', desired_state)
    
    # Sets the specified field to the desired state
    def __set_field_state(self, field, desired_state):
        modified_topics = 0
        for topic in self.__topics:
            if getattr(topic, field) != desired_state:
                setattr(topic, field, desired_state)
                topic.save()   
                modified_topics+=1
        
        return modified_topics