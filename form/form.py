class Form:
    def __init__(self):
        self.fields = {}

    def add_field(self, name, selector, input_type, value=""):
        self.fields[name] = {
            'selector': selector,
            'input_type': input_type,
            'value': value
        }

    def __str__(self):
        out = "Form(\n"
        for name, field in self.fields.items():
            out += f"  {name}: {{selector: {field['selector']}, input_type: {field['input_type']}, value: '{field['value']}'}}\n"
        out += ")"
        return out
