class Processor:

    def __init__(self, net):
        self.net = net
        self.min = set()

        self.events = set()
        self.conditions = set()

        self.conflict_relation = set()
        self.causal_relation_pre = set()
        self.causal_relation_post = set()

        self.cut_off = set()

        self.minimum = {}
        self.configurations_cache = {}
        self.config_length_cache = {}
