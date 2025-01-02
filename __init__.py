import nodes
from nodes.axun_string import NODE_CLASS_MAPPINGS as string_mappings, NODE_DISPLAY_NAME_MAPPINGS as string_display_mappings

# 注册自定义节点
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

NODE_CLASS_MAPPINGS.update(string_mappings)
NODE_DISPLAY_NAME_MAPPINGS.update(string_display_mappings)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
