import argparse

class StoreTrueOrValue(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None:
            setattr(namespace, self.dest, True)
        else:
            setattr(namespace, self.dest, values)

def process_flags( flags ):
    # Step 1: Convert list to dictionary
    parsed_dict = {}
    for list_of_flags in flags:
        for item in list_of_flags:
            if '=' in item:
                key, value = item.split('=', 1)
                parsed_dict[key] = value
            else:
                parsed_dict[item] = None
    # Step 2: Convert dictionary to command-line string
    cmd_parts = []
    for key, value in parsed_dict.items():
        if value is None:
            cmd_parts.append(f"{key}")
        else:
            cmd_parts.append(f"{key}={value}")

    res_flags = ' '.join(cmd_parts)
    
    return res_flags
