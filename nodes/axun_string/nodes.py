import torch

class StringConcat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string1": ("STRING", {"default": ""}),
                "string2": ("STRING", {"default": ""}),
                "separator": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concat"

    CATEGORY = "axun/string"

    def concat(self, string1, string2, separator):
        return (string1 + separator + string2,)
