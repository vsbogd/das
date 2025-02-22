from enum import Enum

class CollectionNames(str, Enum):
    INCOMING_SET = 'incomming_set'
    OUTGOING_SET = 'outgoing_set'
    PATTERNS = 'patterns'
    TEMPLATES = 'templates'
    NAMED_ENTITIES = 'names'
