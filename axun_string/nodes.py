NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

class AXUN_StringNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "axun/string"

    def process(self, text):
        return (text,)

NODE_CLASS_MAPPINGS["AXUN_StringNode"] = AXUN_StringNode
NODE_DISPLAY_NAME_MAPPINGS["AXUN_StringNode"] = "AXUN String Node"
