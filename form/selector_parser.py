from itertools import product
import scraper.selector as sel
from form.form import Form

def build_forms_from_selector_module():
    variable_fields = []
    fixed_fields = []

    for attr in dir(sel):
        if attr.endswith("_SELECTOR"):
            selector = getattr(sel, attr)
            base_name = attr.removesuffix("_SELECTOR")

            input_type_attr = f"{base_name}_INPUT_TYPE"
            input_type = getattr(sel, input_type_attr, "text")

            values_attr = f"{base_name}_VALUES"
            value_attr = f"{base_name}_VALUE"

            field_name = base_name.replace("SEARCH_", "").lower()

            if hasattr(sel, values_attr):
                values = getattr(sel, values_attr)
                variable_fields.append({
                    'name': field_name,
                    'selector': selector,
                    'input_type': input_type,
                    'values': values
                })
            else:
                value = getattr(sel, value_attr, "")
                fixed_fields.append({
                    'name': field_name,
                    'selector': selector,
                    'input_type': input_type,
                    'value': value
                })

    all_combinations = product(*[f['values'] for f in variable_fields])

    forms = []
    for combo in all_combinations:
        form = Form()

        for f, value in zip(variable_fields, combo):
            form.add_field(f['name'], f['selector'], f['input_type'], value)

        for f in fixed_fields:
            form.add_field(f['name'], f['selector'], f['input_type'], f['value'])

        forms.append(form)

    return forms
