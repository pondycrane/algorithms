import abc
import typing
import unittest

class NodeInterface(abc.ABC):
    def __init__(self, name, permission):
        self.name = name
        self.permission = permission
        self.children = []
        self.data = None

    def accept(self, visitor, *args, **kwargs):
        """
        To get subdirectory or files for a directory.
        Should have concrete implementation for Directory class.
        """
        visitor.visit(self, *args, **kwargs)

class File(NodeInterface): pass

class Directory(NodeInterface): pass

class SysLink(NodeInterface):
    def __init__(self, name, permission, target):
        super().__init__(name, permission)
        self.target = target

class NodeVisitorInterface(abc.ABC):
    @abc.abstractmethod
    def visit(self, node: NodeInterface):
        """
        Visit a Node file using defined visit method. This can be
        used for reading or writing or any type of modification of
        the file in Node
        """

class ReadVisitor(NodeVisitorInterface):
    def visit(self, node: NodeInterface):
        if isinstance(node, SysLink) and isinstance(node.target, File):
            print(f'streaming out syslink {node.target.data}')
        elif isinstance(node, File):
            print(f'streaming out file {node.data}')
        else:
            raise ValueError("node has to be a File or SysLink instance")

class WriteVisitor(NodeVisitorInterface):
    def visit(self, node: NodeInterface, data: bytes):
        if isinstance(node, SysLink) and isinstance(node.target, File):
            print(f'writing {bytes} into syslink {node.target}')
        elif isinstance(node, File):
            print(f'writing {bytes} into file {node}')
        else:
            raise ValueError("node has to be a File or SysLink instance")

class AddChildVisitor(NodeVisitorInterface):
    def visit(self, node: NodeInterface, new_node: NodeInterface):
        if not isinstance(node, Directory):
            raise ValueError('Can only add child to Directory objects')

        node.children.append(new_node)

class RemoveChildVisitor(NodeVisitorInterface):
    def visit(self, node: NodeInterface, to_remove: NodeInterface):
        if not isinstance(node, Directory):
            raise ValueError('Can only remove child from a Directory object')

        node.children = [n for n in node.children if n is not to_remove]

class UnitTest(unittest.TestCase):
    def test_file_readable(self):
        f = File('first_file', 'admin')
        f.data = 'file data!'
        read_visitor = ReadVisitor()
        f.accept(read_visitor)

    def test_file_writable(self):
        f = File('first_file', 'admin')
        write_visitor = WriteVisitor()
        f.accept(write_visitor, bytes(3))

    def test_directory_not_readable(self):
        d = Directory('first_directory', 'admin')
        write_visitor = WriteVisitor()
        try:
            d.accept(write_visitor, bytes(3))
        except Exception as e:
            pass
        else:
            raise Exception('No error thrown')

    def test_read_symlink(self):
        f = File('second_file', 'admin')
        f.data = 'linked filed data!'
        s = SysLink('first_symlink', 'admin', f)
        read_visitor = ReadVisitor()
        s.accept(read_visitor)

    def test_add_directory_child(self):
        d = Directory('dir', 'admin')
        to_add = File('file to add', 'admin')
        d.accept(AddChildVisitor(), to_add)
        assert len(d.children) == 1
        
        d.accept(RemoveChildVisitor(), to_add)
        assert not d.children




