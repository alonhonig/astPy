import ast
import codegen
import copy

class Sort:

    def key(self, context):
        return None


class Alphabetical ():

    @staticmethod
    def key(context):
        return context.name

class Length ():

    @staticmethod
    def key(context):
        return len(context.name)


class Unsorted:

    def __init__(self, ast_node, sorter):
        self.context = ast_node
        self.sorter = sorter
        self.grouping = [
            ast.alias,
            ast.Import,
            ast.ImportFrom,
            ast.ClassDef,
            ast.FunctionDef,
            ast.Assign]
        self.mapper = Map(self.sorter)

    def children(self):
        return self.context.body

    def sort(self):
        self.organize()
        self.context.body = self.get_sorted()

    def node_sorter(self, children):    
        s_nodes = {self.sorter.key(n): n for n in children}
        return [s_nodes[n] for n in sorted(s_nodes.keys())]


    def get_sorted(self):
        out = []
        for group_class in self.grouping:
            if group_class in self.groups:
                out.extend(self.node_sorter(self.groups[group_class]))      
        return out

    def organize(self):
        self.groups = {}
        for child in self.children():
            child_type = type(child)
            if child_type not in self.groups:
                self.groups[child_type] = []
            self.mapper.sort(child)
            self.groups[child_type].append(child)


class Map:

    def __init__(self, sorter):
        self.sorter = sorter
        self.class_map = {ast.Assign:Assign,
                          ast.Import: Import,
                          ast.ClassDef:Unsorted}

    def sort(self, ast_node):
        n_type = type(ast_node)
        if n_type in self.class_map:
            u = self.class_map[n_type](ast_node, self.sorter)
            u.sort()


class Import(Unsorted):

    def children(self):
        return self.context.names

    def sort(self):
        sorted_aliases = self.get_sorted()
        self.context.name = ",".join([a.name for a in sorted_aliases])
        self.context.names = sorted_aliases

    def get_sorted(self):
        return self.node_sorter(self.children())    


class Assign(Import):

    def children(self):
        out = []
        for c in self.context.targets:
            c.name = c.id
            out.append(c)
        return out

    def sort(self):
        sorted_targets = self.get_sorted()
        self.context.name = ",".join([a.id for a in sorted_targets])
        self.context.targets = sorted_targets




