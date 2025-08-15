from typing import List, Any

class RouteRegister:
    def __init__(self, route: Any, prefix: str, tags: List[str]):
        self.route = route
        self.prefix = prefix
        self.tags = tags
    route: Any
    prefix: str
    tags: List[str]